# Corpora

If you are interested in obtaining one of the sample corpora for testing purposes, please
complete this form: https://www.iptc.org/get/extra-corpus-downloadform

Upon clicking Submit, you'll be sent to a page from where both corpora can be downloaded. The
download URL is valid for 24 hours

To index a document into a specific corpora:

**POST** */corpora/{corpora_id}/documents*

```json
{
  "id": "tag:reuters.com,0000:newsml_L4N1D22HT_1029243955",
  "title": "China to boost beds, staff to handle healthcare strains",
  "body": "<p> SHANGHAI, Jan 11 (Reuters) - China will add 89,000 new hospital beds and train 140,000 new obstetricians and nurses in order to deal with the strains on its healthcare system brought about in part by the relaxation of its "one-child policy", state media said on Wednesday.</p> <p>Worried about its <span class="highlight">ageing</span> <span class="highlight">population</span>, China issued guidelines in late 2015 allowing all parents to have two children and now needs to meet fresh demand for public services such as child healthcare and primary education, the official Xinhua news agency said.</p> <p>As part of its 2016-2020 health "five-year plan", China aims to raise its total number of nurses to 4.45 million by the end of the decade, Xinhua said.</p> <p>The new plan, published late on Tuesday, said demographic problems were likely to become more pronounced in the coming five years as a result of China's <span class="highlight">ageing</span> <span class="highlight">population</span>, rising urbanisation rates and healthcare coverage gaps in some regions.</p> <p>It said China's average life expectancy was expected to rise one year to 77.3 years by the end of 2020, while its population was forecast to rise to around 1.42 billion, up from 1.37 billion at the end of 2015.</p> <p>China also aims to cut infant mortality rates to less than 18 per 100,000 births, down from 20.1 in 2015, and death rates from diseases such as cancer and diabetes were also expected to fall 10 percent over the 2016-2020 period.   (Reporting by David Stanway) </p>",
  "slugline":"CHINA/HEALTH",
  "versionCreated": "2017-01-11T01:02:20.000Z"
}
```

Note that the document specified in the body must respect the schema of the corpora.
