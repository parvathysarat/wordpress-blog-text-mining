# wordpress-blog-text-mining
Topic modeling and word cloud generation from my WordPress blogposts

Python's <b> wordpress_xmlrpc </b> package suports extracting of WordPress site data, provided you have the <b> address, username and password </b> to your site. 

Here I've extracted all my published wordpress blogposts - 50 of them with a total of 32251 words (it isn't much but I'm hoping to extend this long term so I'll have more data as I publish more :-) ).
There is also an option to extract your drafts in the <b> GetPosts() </b> call.

Modules -
1. Data extraction using <b> wordpress_xmlrpc </b>
2. Word clouds generation using <b> wordcloud </b>- nouns, verbs, adjectives
3. Topic modeling using latent dirichlet allocation (<b>gensim, nltk, spaCy</b>) - 12 generated topics visualized using <b> pyLDAvis </b> (refer<i> topicmodeling_vis.html</i>)

pyLDAvis visualization - http://htmlpreview.github.io/?https://github.com/parvathysarat/wordpress-blog-text-mining/blob/master/index.html
