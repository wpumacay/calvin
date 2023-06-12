# Review: CALVIN Benchmark [^1]

## [**SLIDES**][14]

1. [Introduction](#1-introduction)
2. [Background](#2-background)
    + [Dataset generation via Goal Relabelling](#21-dataset-generation-via-goal-relabelling)
    + [Goal Conditioned Behavior Cloning](#22-goal-conditioned-behavior-cloning)
    + [MultiContext Imitation Learning](#23-multicontext-imitation-learning)
3. [CALVIN benchmark](#3-calvin-benchmark)
    + [CALVIN Environment](#31-calvin-environment)
    + [CALVIN Dataset](#32-calvin-dataset)
4. [Some Results](#4-some-results)
5. [Discussion](#5-discussion)

## 1. Introduction

**CALVIN** [^1] consists of a novel manipulation benchmark for learning **Goal Conditioned**
policies using either goal images or language as free-form text. It includes a
simulated manipulation environment, an annotated dataset taken using teleoperation,
and a baseline algorithm (MCIL) introduced by Lynch & Sermanet [^2].

![calvin_teaser][img_calvin_teaser]

## 2. Background

The authors' work is based on previous work by Lynch & Sermanent [^2] and Lynch
et.al.[^3]. They reproduce the simulated environment introduced by these previous
works, using [PyBullet][3] instead of [MuJoCo][4]. They also collected a similar
dataset as the one presented in [^2], using VR to handle the simulated environment
in data-collection mode. The key takeawayas from these papers are listed below:

- Learning Latent Plans from Play
    + Dataset generation via Goal Relabelling
    + Goal Conditioned Behavior Cloning

- Language Conditioned Imitation Learning over Unstructured Data
    + MultiContext Imitation Learning

### 2.1 Dataset generation via Goal Relabelling

The data collected from Play is later separated into small 1-2 second sequences,
from which the last step of this trajectory is labeled as a goal state which is
used to condition the policy.

[![Clip](https://img.shields.io/badge/clip-YouTube-red)][5]

![method_goal_relabeling][img_goal_relabelling]

### 2.2 Goal Conditioned Behavior Cloning

The key idea of GCBC is to use a conditioning goal state to make the policy follow
a specific task given by the goal image.

[![Clip](https://img.shields.io/badge/clip-YouTube-red)][6]

![method_goal_conditioned_behavior_cloning][img_goal_conditioned_behavior_cloning]

### 2.3 MultiContext Imitation Learning

MCIL key idea is to allow the user to condition using various sources, like goal
images, or goals given by natural language. The idea is to have separate encoders
that map the various contexts into a single latent goal vector.

[![Clip](https://img.shields.io/badge/clip-YouTube-red)][7]

![method_multicontext_imitation_learning][img_multicontext_imitation_learning]

## 3. CALVIN benchmark

### 3.1 CALVIN Environment

CALVIN reproduces the original environment introduced by Lynch & Sermanent [^2]
using the open-source [PyBullet][3] alternative, as [MuJoCo][4] back in the day
was still closed source and most likely the authors of [^2] [^3] weren't allowed
to share their simulated environment.

CALVIN's simulated environment also allows for a wider range of sensors, as
shown below. These include:

* Proprioceptive information (including robot's joint positions, velocities, etc).
* RGB and Depth information from cameras mounted statically in the scene.
* RGB and Depth information from cameras mounted on the gripper frame.
* Vision based tactile sensors.

![calvin_env_observations][img_calvin_env_observations]

To play with the environment, there's a handy [`play_table_env.py`][9] script
that we can use as follows:

```bash
# Go back to where the repository was cloned
cd $CALVIN_ROOT
# Go go the location of the script (some absolute paths must be hard coded :c)
cd calvin_env/calvin_env/envs
# Run the test-env script (spawns the D variant of the environment)
python play_table_env.py
```

![calvin_env][img_calvin_env_setup]

### 3.2 CALVIN Dataset

CALVIN provides a rich dataset collected in a similar fashion to the dataset used
in Lynch & Sermanet [^2]. The authors use also data collection through teleoperation
to reach 24 hours of teleoperated **Play** data, which covers most of the state space
in a similar way to the dataset mentioned before. The only difference in this stage
is that the teleoperated data collected in VR corresponds to the simulated environment
that uses [PyBullet][3], instead of [MuJoCo][4] Haptix, which is the one used
by Lynch & Sermanet [^2].

We can make use of the [`visualize_dataset.py`][8] helper script to visualize the
**Play** data. Below we show some steps from a sample trajectory:

```bash
# Go back to where the repository was cloned
cd $CALVIN_ROOOT
# Run the visualizer pointing to the debug dataset (location of scene_info.npy)
python scripts/visualize_dataset.py dataset/calvin_debug_dataset/training
```

Below there's a sequence that we can analyze using the provided visualizer:

![calvin_dataset_data_1][img_calvin_dataset_1]

## 4. Some Results

Below we show some results obtained from training the `MCIL` baseline on the `Debug`
dataset. We have selected just a few successes and failures of some a few of the
21 tasks.

You can click [here][0] to see some more results logged in **Weights & Biases**

- **Close drawer** (`Successes`)

![close-drawer-success-1][img_results_close_drawer_success_1]
![close-drawer-success-2][img_results_close_drawer_success_2]
![close_drawer-success-3][img_results_close_drawer_success_3]

- **Close drawer** (`Fails`)

![close-drawer-fail-1][img_results_close_drawer_fail_1]
![close-drawer-fail-2][img_results_close_drawer_fail_2]
![close-drawer-fail-3][img_results_close_drawer_fail_3]

- **Lift blue block drawer** (`Fails`)

![lift-blue-block-drawer-fail-1][img_results_lift_blue_block_drawer_fail_1]
![lift-blue-block-drawer-fail-2][img_results_lift_blue_block_drawer_fail_2]
![lift-blue-block-drawer-fail-3][img_results_lift_blue_block_drawer_fail_3]

- **Move slider left** (`Successes`)

![close-drawer-success-1][img_results_move_slider_left_success_1]
![close-drawer-success-2][img_results_move_slider_left_success_2]
![close_drawer-success-3][img_results_move_slider_left_success_3]

- **Move slider left** (`Fails`)

![close-drawer-fails-1][img_results_move_slider_left_fail_1]
![close-drawer-fails-2][img_results_move_slider_left_fail_2]
![close_drawer-fails-3][img_results_move_slider_left_fail_3]

## 5. Discussion

Here the are some comments I have related to the codebase:

### 5.1 Related to the codebase

The authors put quite some effort into making the source code usable mainly via
[Hydra][10], which so far it seems to get in the way of the programmer instead
of helping. I find useful to use a config. system, e.g. I've used [gin-config][11]
quite a lot of times. However, to my view, having every single part being configurable
makes it harder to use without fiddling around with the config files till you get
the expected behavior.

Another take I have is their lack of use of Standard Python guidelines. I even
got to see the following in their codebase. The `sys.path` hack should not be
used and replaced in favour of having your packages being pip installable.

![codebase-bad-usage-of-sys-path][img_bad_usage_of_system_path]

Lastly, I think that their tools and helper scripts should be better documented.
For example: 

- There's no single script I can use without doing lots of changes to just replay
  a policy and input some text to test the results.
- There's no single docs that explain how to load the dataset, or even a well documented
  dataloader that could do the job. Instead, as far as I've checked, there's only
  a single helper scripts that does this job, and one would have to analyze it in
  order to understand how the data is stored as `.npy` files.

### 5.2 Related to the project itself

I would try to change the simulator to [MuJoCo][4], as it's currently open source,
and there's even a repo that contains high quality models for their usage with [MuJoCo][4],
like [MuJoCo Menagerie][12]. Below there's a simulation of the Franka Panda robotic
arm:

![franka-panda-mujoco][img_franka_panda_mujoco]

We could also make use of [Nvidia Isaac Gym][13] as an option for GPU-accelerated
simulation.

## 6. References

[^1]: [Mess, Oier et. al. *CALVIN: A Benchmark for Language-conditioned Policy Learning for Long-horizon Robot Manipulation Tasks*](https://arxiv.org/pdf/2112.03227.pdf)
[^2]: [Lynch, Corey & Sermanet, Pierre. *Language Conditioned Imitation Learning over Unstructured Data*](https://arxiv.org/pdf/2005.07648.pdf)
[^3]: [Lynch, Corey et. al. *Learning Latent Plans from Play*](https://arxiv.org/pdf/1903.01973.pdf)

[//]: # (References)

<!-- URLS -->

[0]: <https://api.wandb.ai/links/rl-loco/k59km9vc> (ref-wandb-report-1)
[1]: <https://learning-from-play.github.io/> (ref-lfp-website)
[2]: <https://language-play.github.io/> (ref-lang-lfp-website)
[3]: <https://pybullet.org/> (ref-bullet-repo)
[4]: <https://mujoco.org/> (ref-mujoco-repo)
[5]: <https://youtu.be/eVK__DeOyrY> (ref-video-yt-goal-relabeling)
[6]: <https://youtu.be/jBpN-ms8wGQ> (ref-video-yt-goal-conditioned-behavior-cloning)
[7]: <https://youtu.be/LrKLSnlUpsk> (ref-video-yt-multicontext-imitation-learning)
[8]: <https://github.com/mees/calvin/blob/main/scripts/visualize_dataset.py> (ref-visualize-script)
[9]: <https://github.com/mees/calvin_env/blob/1431a46bd36bde5903fb6345e68b5ccc30def666/calvin_env/envs/play_table_env.py> (ref-playtable-env-script)
[10]: <https://hydra.cc/> (ref-hydra-website)
[11]: <https://github.com/google/gin-config> (ref-gin-config-repo)
[12]: <https://github.com/deepmind/mujoco_menagerie> (ref-mujoco-menagerie)
[13]: <https://developer.nvidia.com/isaac-gym> (ref-nvidia-isaac-gym)
[14]: <https://docs.google.com/presentation/d/1r03hmisMPr80Js8verMb_-HY7XdbsNouMlw-WLsimT8/edit?usp=sharing> (ref-slides)

<!-- IMAGES -->

[img_calvin_teaser]: images/img_calvin_teaser.png

[gif_calvin_env_1]: images/gif_calvin_environment.gif
[gif_calvin_env_2]: images/gif_calvin_env_full.gif

<!-- TODO: Update these to screenshots from the actual environment-->
[img_calvin_env_setup]: images/gif_calvin_environment.gif
[img_calvin_env_observations]: images/gif_calvin_env_full.gif
[img_calvin_env_sensors]: images/img_calvin_env_sensors.png
[img_calvin_env_actions]: images/gif_calvin_environment.gif

[img_calvin_dataset_1]: images/gif_calvin_dataset_1.gif

[img_goal_conditioned_behavior_cloning]: images/img_goal_conditioned_behavior_cloning.png
[img_goal_relabelling]: images/img_goal_relabelling.png
[img_multicontext_imitation_learning]: images/img_multicontext_imitation_learning.png

[img_results_close_drawer_success_1]: images/img_close_drawer_success_1.gif
[img_results_close_drawer_success_2]: images/img_close_drawer_success_2.gif
[img_results_close_drawer_success_3]: images/img_close_drawer_success_3.gif
[img_results_close_drawer_fail_1]: images/img_close_drawer_fail_1.gif
[img_results_close_drawer_fail_2]: images/img_close_drawer_fail_2.gif
[img_results_close_drawer_fail_3]: images/img_close_drawer_fail_3.gif

[img_results_lift_blue_block_drawer_fail_1]: images/img_lift_blue_block_drawer_fail_1.gif
[img_results_lift_blue_block_drawer_fail_2]: images/img_lift_blue_block_drawer_fail_2.gif
[img_results_lift_blue_block_drawer_fail_3]: images/img_lift_blue_block_drawer_fail_3.gif

[img_results_move_slider_left_success_1]: images/img_move_slider_left_success_1.gif
[img_results_move_slider_left_success_2]: images/img_move_slider_left_success_2.gif
[img_results_move_slider_left_success_3]: images/img_move_slider_left_success_3.gif
[img_results_move_slider_left_fail_1]: images/img_move_slider_left_fail_1.gif
[img_results_move_slider_left_fail_2]: images/img_move_slider_left_fail_2.gif
[img_results_move_slider_left_fail_3]: images/img_move_slider_left_fail_3.gif

[img_bad_usage_of_system_path]: images/img_bad_usage_of_system_path.png
[img_franka_panda_mujoco]: images/gif_franka_panda_mujoco.gif
