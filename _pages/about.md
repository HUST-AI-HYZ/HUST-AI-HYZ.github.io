---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# ℹ️ Short Bio

Hi, I'm Yuanzhe, a master student at University of Califronia, San Diego. I have the great honor of being collaborating with Prof. [Yaoqing Yang](https://sites.google.com/site/yangyaoqingcmu/), Prof. [Julian McAuley](https://cseweb.ucsd.edu/~jmcauley/), Prof. [Zhiting Hu](https://zhiting.ucsd.edu) and Dr. [Ren Pu](https://paulpuren.github.io). 

My current research is focused on

- Understanding the mechanisms, dynamics and generalization of LLM and SciML models via mathematical analysis.
- Memory and Reasoning in LLM & Agent.

<!-- I am actively seeking for <span style="color: red;">**26 Fall CS/ECE PhD Positions**</span>, **research internship** after M.S graduation (about six months), and **collobration opportunities**. 
[[2](https://arxiv.org/abs/2506.06280), [3](https://arxiv.org/abs/2410.12178)]
[[1](https://arxiv.org/abs/2507.05257), [4](https://arxiv.org/abs/2502.00592)]
 -->

# 📖 Educations

<!-- - M.S. in Computer Science and Engineering, University of Califronia, San Diego (UCSD)  &nbsp;  *2024.09 - 2026.03 (Expected)*. 
- *2020.09 - 2024.06*, B.S. in Artificial Intelligence, Innovation Experimental Honor Class, Qiming School, Huazhong University of Science and Technology (HUST). GPA: 3.91/4.0.  -->
<table>
  <tr>
    <td style="width: 60px; border: none; padding: 10px 15px 10px 0;">
      <img src="./images/ucsd_badge.png" width="80">
    </td>
    <td style="border: none; vertical-align: middle;">
      <b>University of California, San Diego (UCSD)</b><br>
      M.S. in Computer Science and Engineering
    </td>
    <td style="text-align: right; border: none; vertical-align: middle; white-space: nowrap;">
      <i>2024.09 - 2026.03 (Expected)</i>
    </td>
  </tr>
  <tr>
    <td style="width: 60px; border: none; padding: 10px 15px 10px 0;">
      <img src="./images/hust_badge.png" width="80">
    </td>
    <td style="border: none; vertical-align: middle;">
      <b>Huazhong University of Science and Technology (HUST)</b><br>
      B.S. in Artificial Intelligence, Innovation Experimental Honor Class, Qiming School<br>
      GPA: 3.91/4.0
    </td>
    <td style="text-align: right; border: none; vertical-align: middle; white-space: nowrap;">
      <i>2020.09 - 2024.06</i>
    </td>
  </tr>
</table>


# 📝 Writing Samples 

(# denotes equal contribution)

## First Authored
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/paper_main/ICML2025_FARMS.jpg' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[1] Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias**

**Yuanzhe Hu**, Kinshuk Goel, Vlad Killiakov, Yaoqing Yang

**ICML 2025**

**Short Summary:** FARMS, a method for normalizing weight matrices by subsampling with a fixed aspect ratio based on M-P Law, improves the accuracy of eigenspectrum analysis and layer-wise hyperparameter assignment across various domains, including image classification, scientific machine learning, and large language model pruning.

[Code](https://github.com/HUST-AI-HYZ/FARMS) \| [Paper and Review](https://openreview.net/forum?id=7ywj1B3DuO&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2025%2FConference%2FAuthors%23your-submissions)) \| [ICML Website](https://icml.cc/virtual/2025/poster/46300)  \| ![Star Count](https://img.shields.io/github/stars/HUST-AI-HYZ/FARMS.svg)


</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024</div><img src='images/paper_main/EMNLP_2024.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[2] Model Balancing Helps Low-data Training and Fine-tuning**

{Zihang Liu#, **Yuanzhe Hu#**}, Tianyu Pang, Yefan Zhou, Pu Ren, Yaoqing Yang

**EMNLP 2024 <span style="color: red;">, Oral (168/6105=2.75%), Meta Review OA=5.0</span>**

**Short Summary:** This paper introduce a modified layer-wise learning rate scheduler, improves low-data training and fine-tuning performance in both NLP and SciML by balancing training quality across model layers.


[Code](https://github.com/ZihangHLiu/ModelBalancing) \| [Paper](https://arxiv.org/abs/2410.12178) \| [Video](https://us06web.zoom.us/rec/play/5RHeJiEVuG-yw_Ytt9cHPMzqEIm2xWenwjhHjJ4yt7camtmQObTndJ56YgBBw0A1TlNRGiwZ2MAw5klz.7Xm2WgzcHdxPjGqm?autoplay=true) \| [Review](./pdf/paper_review/Model_balancing_review.pdf) \| ![Star Count](https://img.shields.io/github/stars/ZihangHLiu/ModelBalancing.svg)


</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/paper_main/MemAgentBench.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[3] Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions**

{**Yuanzhe Hu#**, Yu Wang#}, Julian McAuley

Under Review / **ICML 2025 LCFM Workshop**

**Short Summary:**  MemoryAgentBench is a new benchmark designed to evaluate four core competencies of memory agents in Large Language Models, highlighting the need for improved memory mechanisms.


[HF Dataset](https://huggingface.co/datasets/ai-hyz/MemoryAgentBench) \| [Code](https://github.com/HUST-AI-HYZ/MemoryAgentBench) \| [Paper](https://arxiv.org/abs/2507.05257) \| ![Star Count](https://img.shields.io/github/stars/HUST-AI-HYZ/MemoryAgentBench.svg)


</div>
</div>

## Contributed
<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report</div><img src='images/paper_main/K2-Think.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[4] K2-Think: A Parameter-Efficient Reasoning System**

Zhoujun Cheng, Richard Fan, Shibo Hao, Taylor W. Killian, Haonan Li, Suqi Sun, Hector Ren, Alexander Moreno, Daqian Zhang, Tianjun Zhong, Yuxin Xiong, **Yuanzhe Hu**, Yutao Xie, Xudong Han, Yuqi Wang, Varad Pimpalkhute, Yonghao Zhuang, Aaryamonvikram Singh, Xuezhi Liang, Anze Xie, Jianshu She, Desai Fan, Chengqian Gao, Liqun Ma, Mikhail Yurochkin, John Maggs, Xuezhe Ma, Guowei He, Zhiting Hu, Zhengzhong Liu, Eric P. Xing

**MBZUAI IFM / LLM 360 Tech Report**


**Short Summary:** K2-Think introduces a parameter-efficient reasoning system based on a 32B model, achieving state-of-the-art mathematical reasoning scores by synergistically combining advanced post-training and strategic test-time computation techniques. The system, leveraging Cerebras Wafer-Scale Engine, delivers a micro-average of 67.99 on challenging math benchmarks, outperforming much larger open-source models while enabling 10x faster inference.


[NY Times](https://www.nytimes.com/2025/09/09/technology/uae-emirates-ai-open-source.html) \| [Forbes](https://www.forbes.com/sites/patrickmoorhead/2025/09/09/the-uae-showcases-its-abilities-in-ai-reasoning-with-k2-think-model/) \| [HF Model](https://huggingface.co/LLM360/K2-Think) \| [Code](https://github.com/MBZUAI-IFM/K2-Think-SFT) \| [Paper](https://arxiv.org/abs/2509.07604) \| ![Star Count](https://img.shields.io/github/stars/MBZUAI-IFM/K2-Think-SFT.svg)


</div>
</div> -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/paper_main/ICML2025_Mplus.jpg' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[4] M+: Extending MemoryLLM with Scalable Long-Term Memory**

Yu Wang, Dmitry Krotov, **Yuanzhe Hu**, Yifan Gao, Wangchunshu Zhou, Julian McAuley, Dan Gutfreund, Rogerio Feris, Zexue He

**ICML 2025**


**Short Summary:** M+ enhances long-term information retention in large language models by integrating a retriever-based long-term memory mechanism, outperforming MemoryLLM and other baselines in knowledge retention tasks.


[机器之心](https://mp.weixin.qq.com/s/8fl3ymmJMn2P0_XBmVQQuw) \| [HF Model](https://huggingface.co/YuWangX/mplus-8b) \| [Code](https://github.com/wangyu-ustc/MemoryLLM) \| [Paper](https://arxiv.org/abs/2502.00592) \| [Review](https://openreview.net/forum?id=OcqbkROe8J&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2025%2FConference%2FAuthors%23your-submissions)) \| ![Star Count](https://img.shields.io/github/stars/wangyu-ustc/MemoryLLM.svg)


</div>
</div>


# 🔥 News
<!-- - *2025.09*: &nbsp;😁 Excited to share that our recent work "K2-Think: A Parameter-Efficient Reasoning System", which was report by NY Times and Forbes. -->
- *2025.07*: &nbsp;😁 We open-sourced the [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench). Thanks for the great help from [Yu Wang](https://yuwang.us)! 
- *2025.05*: &nbsp;🎉🎉 Two papers are accepted by [ICML 2025](https://icml.cc/) as **Poster**! See you at Vancouver.
- *2024.09*: &nbsp;🎉🎉 Excited to share that our work “Model Balancing Helps Low-data Training and Fine-tuning” is accepted by [EMNLP 2024](https://2024.emnlp.org) as **Oral Presentation**!
- *2024.06*: &nbsp;😁 I graduated from HUST!
- *2024.06*: &nbsp;😄 I created my account on OpenReview!

Last Update: 09/2025

