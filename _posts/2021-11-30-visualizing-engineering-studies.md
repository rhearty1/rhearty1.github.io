---
layout: post
title: Visualizing the community of engineering studies scholars
categories: [coding]
tags: [history, engineering]
---

I generated a co-citation network for the journal, *Engineering Studies*. Co-citation is defined as the frequency with which two documents are cited together by other documents. To explore the graph, [download this pdf](/assets/engineering-studies-co-citation/es.pdf), or if you have Gephi, click [here](/assets/engineering-studies-co-citation/es.gephi).

![](/assets/engineering-studies-co-citation/es.svg)

What I did this time:
1.	Using Web of Science, I downloaded all 173 articles published in Engineering Studies from its inception in 2009 until 30 November 2021.
2.	Created a co-citation network using Sci2tool and [this tutorial](http://scottbot.net/networks-demystified-7-doing-co-citation-analyses/)([archived version](https://www.scottbot.net/HIAL/index.html@p=39432.html)) by Scott Weingart.
3.	In Sci2tool, I removed any edge between articles unless they’ve been cited together more than once.
4.	In Sci2tool, I removed any remaining isolated components and the small islands, focusing instead on the “blob,” the single strongly connected component shown here.
5.	In Gephi, I clarified the visualization using [these suggestions](https://www.youtube.com/watch?v=f6ElMvP7ubs). For instance, I color-coated based on modularity class (clusters of articles that tended to be cited together more often than others).

There were a few modularity classes. The largest, in purple, was greatly influenced by the work of Wendy Faulkner.

![](/assets/engineering-studies-co-citation/purple.png)

Next largest were in blue, green, orange, and gray.

![](/assets/engineering-studies-co-citation/blue.png)

![](/assets/engineering-studies-co-citation/green.png)

![](/assets/engineering-studies-co-citation/orange.png)

![](/assets/engineering-studies-co-citation/gray.png)

Two smaller ones worth noting are in light gray and pink.

![](/assets/engineering-studies-co-citation/light-gray.png)

![](/assets/engineering-studies-co-citation/pink.png)
