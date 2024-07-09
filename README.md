# Reference:
- https://github.com/robotgradient/grasp_diffusion?tab=readme-ov-file

# Settings
1. Conda env
   1. conda env create -f ./grasp_diffusion/environment.yml -n py38
   2. conda activate py38
   3. pip3 install -r ./grasp_diffusion/requirements.txt

반드시 mesh_to_sdf 파일에서 pip3 install -e . 한번 실행

tensorboard --logdir=/home/irsl/24-se3-df/logs/multiobject_p_graspdif/summaries
