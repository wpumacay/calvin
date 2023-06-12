# Review: CALVIN Benchmark [^1]

1. [Introduction](#1-introduction)
2. [Background](#2-background)
    + [Dataset generation via Goal Relabelling](#21-dataset-generation-via-goal-relabelling)
    + [Goal Conditioned Behavior Cloning](#22-goal-conditioned-behavior-cloning)
    + [MultiContext Imitation Learning](#23-multicontext-imitation-learning)
3. [CALVIN benchmark](#3-calvin-benchmark)
    + [CALVIN Environment](#31-calvin-environment)
    + [CALVIN Dataset](#32-calvin-dataset)
4. [Some Results](#4-some-results)

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

[![Clip](https://img.shields.io/badge/clip-YouTube-red)][5]

![method_goal_relabeling][img_goal_relabelling]

### 2.2 Goal Conditioned Behavior Cloning

[![Clip](https://img.shields.io/badge/clip-YouTube-red)][6]

![method_goal_conditioned_behavior_cloning][img_goal_conditioned_behavior_cloning]

### 2.3 MultiContext Imitation Learning

[![Clip](https://img.shields.io/badge/clip-YouTube-red)][7]

![method_multicontext_imitation_learning][img_multicontext_imitation_learning]

## 3. CALVIN benchmark

### 3.1 CALVIN Environment

![calvin_env][img_calvin_env_setup]

#### 3.1.1 Observations

![calvin_env_observations][img_calvin_env_observations]

#### 3.1.2 Actions

![calvin_env_actions][img_calvin_env_actions]

### 3.2 CALVIN Dataset

CALVIN provides a rich dataset collected in a similar fashion to the dataset used
in Lynch & Sermanet [^2]. The authors use also data collection through teleoperation
to reach 24 hours of teleoperated **Play** data, which covers most of the state space
in a similar way to the dataset mentioned before. The only difference in this stage
is that the teleoperated data collected in VR corresponds to the simulated environment
that uses PyBullet, instead of MuJoCo Haptix, which is the one used by Lynch &
Sermanet [^2].

We can make use of the `visualize_dataset.py` helper script to visualize the
**Play** data. Below we show some steps from a sample trajectory:

```bash
# Go back to where the repository was cloned
cd $CALVIN_ROOOT
# Run the visualizer pointing to the debug dataset (location of scene_info.npy)
python scripts/visualize_dataset.py dataset/calvin_debug_dataset/training
```

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



## 5. References

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

<!-- VIDEOS -->

<!-- https://youtu.be/jBpN-ms8wGQ -->

<!-- IMAGES -->

[img_calvin_teaser]: images/img_calvin_teaser.png

[gif_calvin_env_1]: images/gif_calvin_environment.gif
[gif_calvin_env_2]: images/gif_calvin_env_full.gif

<!-- TODO: Update these to screenshots from the actual environment-->
[img_calvin_env_setup]: images/gif_calvin_environment.gif
[img_calvin_env_observations]: images/gif_calvin_environment.gif
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
