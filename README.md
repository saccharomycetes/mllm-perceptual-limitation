# Exploring Perceptual Limitation of Multimodal Large Language Models
Code and data for paper 'Exploring Perceptual Limitation of Multimodal Large Language Models'

[Jiarui Zhang](https://saccharomycetes.github.io/), [Jinyi Hu](https://jameshujy.github.io/), [Mahyar Khayatkhoei](https://mahyarkoy.github.io/),  [Filip Ilievski](https://www.ilievski.info/), [Maosong Sun](https://www.cs.tsinghua.edu.cn/csen/info/1180/4033.htm)

[[paper]](https://arxiv.org/pdf/2402.07384.pdf)

# Datasets Creation

The following command will help you create all the images used for the experiments.(BLIP-2 and Instruct-BLIP use the same dataset due to the same resolusion.)
```
bash create.sh
```

# Running experiment

Run the 5 models on the dataset:
```
bash run.sh
```

# Evaluate and draw the plots
Then we can use the code in exp_plots.ipynb to evaluate the performance and draw the plots.


# Cite 

If you find our work to be useful in your research, please consider citing the following paper:

```
@misc{zhang2024exploring,
      title={Exploring Perceptual Limitation of Multimodal Large Language Models}, 
      author={Jiarui Zhang and Jinyi Hu and Mahyar Khayatkhoei and Filip Ilievski and Maosong Sun},
      year={2024},
      eprint={2402.07384},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Contact

-   `jzhang37@usc.edu`