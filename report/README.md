# Review: CALVIN Benchmark [^1]

## TL;DR

**CALVIN** consists of a novel manipulation benchmark for learning **Goal Conditioned**
policies using either goal images or language as free-form text.

## 1. Intro

CALVIN consists of a new simulated environment that will serve as benchmark,
which is based on the Franka Panda robotic arm. It heavily builds upon the work
by Lynch & Sermanet [^2], by using the same type of environment and their
proposed new method as baseline.

## 2. Background

This paper is based on the previous work by Lynch & Sermanent [^2] and Lynch
et.al.[^3]. The key takeaways from these papers are:

- Learning Latent Plans from Play
    + Goal Conditioned Behavior Cloning
    + Dataset generation via Goal Relabelling

- Language Conditioned Imitation Learning over Unstructured Data
    + MultiContext Imitation Learning

### 2.1 Goal Conditioned Behavior Cloning (GCBC)

![method_goal_conditioned_behavior_cloning][img_goal_conditioned_behavior_cloning]

### 2.2 Dataset generation via Goal Relabelling

### 2.3 MultiContext Imitation Learning (MCIL)


## 3. CALVIN benchmark

![calvin_env][gif_calvin_env_1]

## 4. Some results

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

<!-- IMAGES -->

[gif_calvin_env_1]: images/gif_calvin_environment.gif

[img_goal_conditioned_behavior_cloning]: images/img_goal_conditioned_behavior_cloning.png

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
