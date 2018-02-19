# plotly-worldmap-mapping-2letter-CountryCode-to-3letter-country-code

[Plotly](https://plot.ly/python/choropleth-maps/) has made it simple to draw the GEO data. Since this chart uses 3 letter country code some of the users may only have 2 letter country code comming to you in the data. There was a questions on this on [stackoverflow](https://stackoverflow.com/questions/38523559/is-it-possible-to-make-plotly-choropleth-use-iso-3166-1-alpha-2-country-codes-in/44895115#44895115) and I also ended up in the same situation. My approach was to download a mapping of country, 2letter country code, 3 letter country code and join the data based on 2 letter country code to get 3 letter country code and the country name for displying the results on the world map. I hope it is helpful for you as well in a this situation. 

![](https://github.com/gsnaveen/plotly-worldmap-mapping-2letter-CountryCode-to-3letter-country-code/blob/master/plotly-worldmap.png)
