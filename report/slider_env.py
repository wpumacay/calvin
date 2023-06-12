#!/usr/bin/env python

# Env. wrapper adapted from:
# https://github.com/mees/calvin/blob/main/RL_with_CALVIN.ipynb

import os
import sys
import gym
import time
import hydra
import numpy as np

from stable_baselines3 import SAC

import pdb

if 'CALVIN_ROOT' not in os.environ:
    print('Must set the env. variable CALVIN_ROOT to the root of the repo')
    sys.exit(1)

ENV_CONFIG_PATH = os.getenv('CALVIN_ROOT')

from calvin_env.envs.play_table_env import PlayTableSimEnv

class SlideEnv(PlayTableSimEnv):

    def __init__(self, tasks, **kwargs):
        super(SlideEnv, self).__init__(**kwargs)
        # Action space is a tensor of shape (7,), containing the following
        # information:
        # - Position of the end effector in World space (x, y, z)
        # - Orientation of the end effector (euler angles) in radians (r, p, y)
        # - Gripper action, either open (1) or close (-1)
        self.action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(7,))

        # Observation space is a tensor of shape (7,), containing the pose of
        # the end effector (position + quaternion)
        self.observation_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(7,))

        # Grab the tasks information
        self.tasks = hydra.utils.instantiate(tasks.copy())

    def reset(self):
        obs = super().reset()
        self.start_info = self.get_info()
        return obs

    def get_obs(self):
        """Overwrite robot obs to only retrieve end effector position"""
        robot_obs, robot_info = self.robot.get_observation()
        return robot_obs[:7]

    def _success(self):
        """ Returns a boolean indicating if the task was performed correctly """
        current_info = self.get_info()
        task_filter = ["move_slider_left"]
        task_info = self.tasks.get_task_info_for_set(self.start_info, current_info, task_filter)
        return 'move_slider_left' in task_info

    def _reward(self):
        """ Returns the reward function that will be used 
        for the RL algorithm """
        reward = int(self._success()) * 10
        r_info = {'reward': reward}
        return reward, r_info

    def _termination(self):
        """ Indicates if the robot has reached a terminal state """
        success = self._success()
        done = success
        d_info = {'success': success}
        return done, d_info

    def step(self, action):
            # Transform gripper action to discrete space
            env_action = action.copy()
            env_action[-1] = (int(action[-1] >= 0) * 2) - 1


            self.robot.apply_action(env_action)
            for i in range(self.action_repeat):
                self.p.stepSimulation(physicsClientId=self.cid)
            obs = self.get_obs()
            info = self.get_info()
            reward, r_info = self._reward()
            done, d_info = self._termination()
            info.update(r_info)
            info.update(d_info)
            return obs, reward, done, info

@hydra.main(config_path=f'{ENV_CONFIG_PATH}/calvin_env/conf',
            config_name='config_data_collection')
def run_env(cfg):
    new_env_cfg = {**cfg.env}
    new_env_cfg['tasks'] = cfg.tasks
    new_env_cfg['use_egl'] = False
    new_env_cfg['show_gui'] = True
    new_env_cfg['use_vr'] = False
    new_env_cfg['use_scene_info'] = True
    new_env_cfg.pop('_target_', None)
    new_env_cfg.pop('_recursive_', None)

    env = SlideEnv(**new_env_cfg)

    model = SAC('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=10000, log_interval=4)


if __name__ == '__main__':
    run_env()
