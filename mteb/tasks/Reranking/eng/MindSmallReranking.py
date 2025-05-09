from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskReranking import AbsTaskReranking


class MindSmallReranking(AbsTaskReranking):
    metadata = TaskMetadata(
        name="MindSmallReranking",
        description="Microsoft News Dataset: A Large-Scale English Dataset for News Recommendation Research",
        reference="https://msnews.github.io/assets/doc/ACL2020_MIND.pdf",
        dataset={
            "path": "mteb/mind_small",
            "revision": "59042f120c80e8afa9cdbb224f67076cec0fc9a7",
        },
        type="Reranking",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="map",
        date=("2019-10-12", "2019-11-22"),
        domains=["News", "Written"],
        task_subtypes=[],
        license="https://github.com/msnews/MIND/blob/master/MSR%20License_Data.pdf",
        annotations_creators="expert-annotated",
        dialect=[],
        sample_creation="found",
        prompt="Retrieve relevant news articles based on user browsing history",
        bibtex_citation=r"""
@inproceedings{wu-etal-2020-mind,
  abstract = {News recommendation is an important technique for personalized news
service. Compared with product and movie recommendations which have been comprehensively studied,
the research on news recommendation is much more limited, mainly due to the lack of a high-quality benchmark
dataset. In this paper, we present a large-scale dataset named MIND for news recommendation. Constructed from
the user click logs of Microsoft News, MIND contains 1 million users and more than 160k English news
articles, each of which has rich textual content such as title, abstract and body. We demonstrate MIND a good
testbed for news recommendation through a comparative study of several state-of-the-art news recommendation
methods which are originally developed on different proprietary datasets. Our results show the performance of
news recommendation highly relies on the quality of news content understanding and user interest modeling.
Many natural language processing techniques such as effective text representation methods and pre-trained
language models can effectively improve the performance of news recommendation. The MIND dataset will be
available at https://msnews.github.io.},
  address = {Online},
  author = {Wu, Fangzhao  and Qiao, Ying  and Chen, Jiun-Hung  and Wu, Chuhan  and Qi,
Tao  and Lian, Jianxun  and Liu, Danyang  and Xie, Xing  and Gao, Jianfeng  and Wu, Winnie  and Zhou, Ming},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  doi = {10.18653/v1/2020.acl-main.331},
  editor = {Jurafsky, Dan  and Chai, Joyce  and Schluter, Natalie  and Tetreault, Joel},
  month = jul,
  pages = {3597--3606},
  publisher = {Association for Computational Linguistics},
  title = {{MIND}: A Large-scale Dataset for News
Recommendation},
  url = {https://aclanthology.org/2020.acl-main.331},
  year = {2020},
}
""",
    )
