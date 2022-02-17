This is a students project from National Yang Ming Chiao Tung University. We are still working on it.

# Train
To train model, please run
```
python train.py --config {DATASET}.yml --imp {DATASET_PATH} --exp {PROJECT_PATH} --doc {MODEL_NAME} --ni
```
# Evalute
To evalute result, please run
```
python infer.py --exp ./runs/ --config bedroom.yml --sample -i images --npy_name lsun_bedroom1 --sample_step 3 --t 500  --ni 
```

# Acknowledgments
This code is heavily borrows from [SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations](https://github.com/ermongroup/SDEdit) and [Denoising Diffusion Implicit Models (DDIM)](https://github.com/ermongroup/ddim). Also we refer to other open sources, such as, [Bridging the Visual Gap: Wide-Range Image Blending](https://github.com/julia0607/Wide-Range-Image-Blending) and [InfinityGAN: Towards Infinite-Resolution Image Synthesis](https://github.com/hubert0527/infinityGAN?fbclid=IwAR0qjeImOUq6IssyTMqYQjLO_pi9e5RT5eQvC92G5YFXUbkfQC_vh2CI9V4) to develop further functions.
