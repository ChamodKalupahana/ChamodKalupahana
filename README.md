
# Hi there 👋

Physics MSci Graduate Becoming A Full Stack Engineer developing iOS, Android and Web App. Specialised In Image Generation AI.

🔭 I’m currently working at International Celebrity Networks (ICN)

📫 How to reach me: www.linkedin.com/in/chamod-kalupahana

# My latest project: Simulating the Universe using Diffusion 🌌

### Problem: The Universe is hard to simulate

To test the physics of different theories of the universe, we need simulations. To get simulations, we need supercomputers... Or do we? Generative AI is incredibly powerful and we're going to use diffusion to speed up the theoretical testing of physics! 

### Dataset: Open-source simulations

This project uses the CAMELs CMD dataset which includes over 150,000 2D simulations of the universe. Each image is a universe that has different starting parameters which determine how the universe evolves. Determining how the universe evolves can be done in two ways:

- N-body
- Hydrodynamical ($M_{gas}$, $V_{gas}$, $T$...)

Hydrodynamical simulations are more physically realistic than N-body simulations but are much more computationally complex to simulate, typically requiring supercomputers.

<img src="Figures\Example fields.jpg" width="600"/>

Perhaps there's a way to convert the simple N-body simulations to realistic Hydrodynamical maps? 🤔 

## Model: Guassian Diffusion

A Diffusion model starts with an image of random noise and the model learns from the training dataset to slowly remove sections of the noise in the image until a clear denoised image is generated.

<img src="Figures\Novel_N_body_Diffusion_Gif.jpg" width="600"/>

The way the diffusion model denoises the image depends on the particular pixel values of the starting image. Since the starting image is random, it acts as a 'seed'  and generates a new random and slightly different image for every output.

This is where the magic happens...

By adding the pixel values of the N-body (training dataset)image to the starting image, and setting the hydrodynamical image as the truth, we can guide the model to 'denoise' the N-body into a hydrodynamical one.

Of course, this is harder said than done and the model takes around 45 mins just to train on 10% of the training dataset. But the results below are remarkably similar.

<img src="Figures\Conditional_Diffusion_6_fields.jpg" width="800"/>

## Model: Architecture 

The technical details can get very overwhelming so I made sure to avoid them here and instead provide a summary here. The full details and report are provided here: [Simulating the Universe Report](Simulating_the_Universe_Report.pdf)

<center>
<img src='Figures\Condition Diffusion N-body to Hydro Arch (1).jpg' width=400/>
</center>

Earlier I simplified the concept of generating a random image. In reality, the truth hydrodynamical map is 'noised' up by the model in the forward process, and then the model learns to remove the noise that was added.

The diffusion model also uses a U-net which is an image-to-image neural network built with convolution layers.

## Results: The Universe is hard to simulate... but it's possible

The hydrodynamical simulations shown above normally require supercomputer processing over days and weeks to produce but this diffusion model can cut that down to a matter of hours. Analysing the generated results and comparing their physical significance, we can see that the model outputs are similar and physically correct! Perhaps we can improve the generation time but this is a new era of universe simulations.


## Thank you for reading 🙏

<!--
**ChamodKalupahana/ChamodKalupahana** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
