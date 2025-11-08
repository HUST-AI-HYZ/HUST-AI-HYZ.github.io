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

Hi, I'm Yuanzhe, a master student at University of Califronia, San Diego. I have the great honor of being collaborating with Prof. [Yaoqing Yang](https://sites.google.com/site/yangyaoqingcmu/), [Julian McAuley](https://cseweb.ucsd.edu/~jmcauley/), [Zhiting Hu](https://zhiting.ucsd.edu), and Dr. [Ren Pu](https://paulpuren.github.io), [Yu Wang](https://yuwang.us), [Zexue He](https://zexuehe.github.io)

My current research is focused on

- Understanding the mechanisms, dynamics and generalization of LLM pruning and post-training via mathematical analysis.
- Memory and Reasoning in LLM & Agent.

I am actively seeking for <span style="color: red;">**26 Fall CS/ECE/DS PhD Positions**</span>, **industrial research internship** after M.S graduation (about six months), and **collobration opportunities** on Agentic Learning. Feel free to reach out! 

# 📖 Educations
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

# ⚙️ Open Source Project

<table>
  <tr>
    <td style="width: 80px; border: none; padding: 10px 15px 10px 0;">
      <img src="./images/mirix_logo.png" width="180">
    </td>
    <td style="border: none; vertical-align: middle;">
      <b>MIRIX: Multi-Agent Memory System for LLM-Based Agents</b><br>
      My Contribution: Designed the framework for MIRIX's Evaluation, project maintenance and bug solving.<br><br>
      <a href="https://mirix.io"><img src="https://img.shields.io/badge/Website-mirix.io-A569BD?logo=googlechrome&logoColor=white" alt="Website"></a>
      <a href="https://github.com/Mirix-AI/MIRIX"><img src="https://img.shields.io/github/stars/Mirix-AI/MIRIX.svg" alt="Star Count"></a>
      <a href="https://github.com/Mirix-AI/MIRIX"><img src="https://img.shields.io/github/forks/Mirix-AI/MIRIX.svg" alt="Fork Count"></a>
    </td>
  </tr>
</table>



# 📝 Writing Samples 

## Leading Authored

<span style="color: #5DADE2;"># denotes equal contribution</span>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/paper_main/ICML2025_FARMS.jpg' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[1] Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias**

**Yuanzhe Hu**, Kinshuk Goel, Vlad Killiakov, Yaoqing Yang

**ICML 2025**

**Short Summary:** A layer-wise LLM pruning method inspired by Marchenko–Pastur (MP) law. 

[Paper](https://arxiv.org/abs/2506.06280) \| [Video](https://icml.cc/virtual/2025/poster/46300) \| [Review](https://openreview.net/forum?id=7ywj1B3DuO&referrer=%5BAuthor%20Console%5D%2Fgroup%3Fid%3DICML.cc%2F2025%2FConference%2FAuthors%23your-submissions)  

<a href="https://github.com/HUST-AI-HYZ/FARMS"><img src="https://img.shields.io/github/stars/HUST-AI-HYZ/FARMS.svg" alt="Star Count"></a>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024</div><img src='images/paper_main/EMNLP_2024.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[2] Model Balancing Helps Low-data Training and Fine-tuning**

{Zihang Liu#, **Yuanzhe Hu#**}, Tianyu Pang, Yefan Zhou, Pu Ren, Yaoqing Yang

**EMNLP 2024 <span style="color: red;">, Oral (168/6105=2.75%), Meta Review OA=5.0</span>**

**Short Summary:** Learning rate scheduler for LLM fine-tuning on low-source dataset. 


[Paper](https://arxiv.org/abs/2410.12178) \| [Video](https://us06web.zoom.us/rec/play/5RHeJiEVuG-yw_Ytt9cHPMzqEIm2xWenwjhHjJ4yt7camtmQObTndJ56YgBBw0A1TlNRGiwZ2MAw5klz.7Xm2WgzcHdxPjGqm?autoplay=true) \| [Review](./pdf/paper_review/Model_balancing_review.pdf)

<a href="https://github.com/ZihangHLiu/ModelBalancing"><img src="https://img.shields.io/github/stars/ZihangHLiu/ModelBalancing.svg" alt="Star Count"></a>


</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/paper_main/MemAgentBench.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[3] Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions**

{**Yuanzhe Hu#**, Yu Wang#}, Julian McAuley

Under Review / **ICML 2025 LCFM Workshop**

**Short Summary:**  MemoryAgentBench is a new benchmark designed to comprehensively evaluate memory agents in LLMs. 


[Paper](https://arxiv.org/abs/2507.05257v2)

<a href="https://github.com/HUST-AI-HYZ/MemoryAgentBench"><img src="https://img.shields.io/github/stars/HUST-AI-HYZ/MemoryAgentBench.svg" alt="Star Count"></a> <a href="https://huggingface.co/datasets/ai-hyz/MemoryAgentBench"><img src="https://img.shields.io/badge/Dataset-HuggingFace-FFD21E?logo=huggingface" alt="HF Dataset"></a> <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fdatasets%2Fai-hyz%2FMemoryAgentBench%3Fexpand%255B%255D%3DdownloadsAllTime&query=%24.downloadsAllTime&label=Total%20Downloads&color=orange&logo=huggingface&cacheSeconds=3600" alt="Dataset Downloads"> 



</div>
</div>

## Contributed

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/paper_main/Mem_Alpha.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[4] Mem-$\alpha$: Learning Memory Construction via Reinforcement Learning**

Yu Wang, Ryuichi Takanobu, Zhiqi Liang, Yuzhen Mao, **Yuanzhe Hu**, Julian McAuley, Xiaojian Wu

**Under Review**


**Short Summary:** Mem-alpha, a reinforcement learning framework, enhances memory management in LLMs through interaction and feedback.


[Paper](https://arxiv.org/abs/2509.25911) 

<a href="https://github.com/wangyu-ustc/Mem-alpha"><img src="https://img.shields.io/github/stars/wangyu-ustc/Mem-alpha.svg" alt="Star Count"></a>  <a href="https://mp.weixin.qq.com/s/a030XuwxVrVZBbrR8qfxNQ"><img src="https://img.shields.io/badge/Media-量子位-1ABC9C?logo=wechat" alt="量子位"></a>  <a href="https://mp.weixin.qq.com/s/O9vmwD_khWfMa785xolJsw"><img src="https://img.shields.io/badge/Media-机器之心-1ABC9C?logo=wechat" alt="机器之心"></a>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report</div><img src='images/paper_main/K2-Think.png' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[5] K2-Think: A Parameter-Efficient Reasoning System**

Zhoujun Cheng, Richard Fan, Shibo Hao, Taylor W. Killian, Haonan Li, Suqi Sun, Hector Ren, Alexander Moreno, Daqian Zhang, Tianjun Zhong, Yuxin Xiong, **Yuanzhe Hu**, Yutao Xie, Xudong Han, Yuqi Wang, Varad Pimpalkhute, Yonghao Zhuang, Aaryamonvikram Singh, Xuezhi Liang, Anze Xie, Jianshu She, Desai Fan, Chengqian Gao, Liqun Ma, Mikhail Yurochkin, John Maggs, Xuezhe Ma, Guowei He, Zhiting Hu, Zhengzhong Liu, Eric P. Xing

**MBZUAI IFM / LLM 360 Tech Report**


**Short Summary:** K2-Think is a parameter-efficient reasoning system based on a 32B model.


[Paper](https://arxiv.org/abs/2509.07604) 

 <a href="https://huggingface.co/LLM360/K2-Think"><img src="https://img.shields.io/badge/Model-HuggingFace-FFD21E?logo=huggingface" alt="Model"></a> <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2FLLM360%2FK2-Think%3Fexpand%255B%255D%3DdownloadsAllTime&label=Total%20Downloads&query=%24.downloadsAllTime&color=orange&logo=huggingface&cacheSeconds=3600" alt="Model Downloads">  <a href="https://www.nytimes.com/2025/09/09/technology/uae-emirates-ai-open-source.html"><img src="https://img.shields.io/badge/Media-NY_Times-555555?logo=nytimes" alt="NY Times"></a> <a href="https://www.forbes.com/sites/patrickmoorhead/2025/09/09/the-uae-showcases-its-abilities-in-ai-reasoning-with-k2-think-model/"><img src="https://img.shields.io/badge/Media-Forbes-5DADE2?logo=forbes" alt="Forbes"></a> 

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/paper_main/ICML2025_Mplus.jpg' alt="sym" width="80%"></div></div>
<div class='paper-box-text' markdown="1">

**[6] M+: Extending MemoryLLM with Scalable Long-Term Memory**

Yu Wang, Dmitry Krotov, **Yuanzhe Hu**, Yifan Gao, Wangchunshu Zhou, Julian McAuley, Dan Gutfreund, Rogerio Feris, Zexue He

**ICML 2025**


**Short Summary:** M+ enhances long-term information retention in LLMs by integrating a retriever-based long-term memory mechanism.

[Paper](https://arxiv.org/abs/2502.00592) \| [Review](https://openreview.net/forum?id=OcqbkROe8J&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2025%2FConference%2FAuthors%23your-submissions)) 

<a href="https://huggingface.co/YuWangX/mplus-8b"><img src="https://img.shields.io/badge/Model-HuggingFace-FFD21E?logo=huggingface" alt="Model"></a> <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2FYuWangX%2Fmplus-8b%3Fexpand%255B%255D%3DdownloadsAllTime&label=Total%20Downloads&query=%24.downloadsAllTime&color=orange&logo=huggingface&cacheSeconds=3600" alt="Model Downloads">    <a href="https://github.com/wangyu-ustc/MemoryLLM"><img src="https://img.shields.io/github/stars/wangyu-ustc/MemoryLLM.svg" alt="Star Count"></a>    <a href="https://mp.weixin.qq.com/s/8fl3ymmJMn2P0_XBmVQQuw"><img src="https://img.shields.io/badge/Media-机器之心-1ABC9C?logo=wechat" alt="机器之心"></a>


</div>
</div>


# 🔥 News
- *2025.09*: &nbsp;😁 Excited to share that our recent work "K2-Think: A Parameter-Efficient Reasoning System".
- *2025.07*: &nbsp;😁 We open-sourced the [MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench). Thanks for the great help from [Yu Wang](https://yuwang.us)! 
- *2025.05*: &nbsp;🎉🎉 Two papers are accepted by [ICML 2025](https://icml.cc/) as **Poster**! See you at Vancouver.
- *2024.09*: &nbsp;🎉🎉 Excited to share that our work “Model Balancing Helps Low-data Training and Fine-tuning” is accepted by [EMNLP 2024](https://2024.emnlp.org) as **Oral Presentation**!
- *2024.06*: &nbsp;😁 I graduated from HUST!
- *2024.06*: &nbsp;😄 I created my account on OpenReview!

Last Update: 11/2025

