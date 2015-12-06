///**
// * Created by SJD on 11/23/2015.
// */
//$("button").click(function(){
//    $.getJSON("eg1.json", function(obj){
//        $.each(obj, function(key, value){
//            $("ul").append("<li>"+value.url+"</li>");
//        });
//    });
//})
//
//
//with((window))
//$.getJSON("https://access.alchemyapi.com/calls/data/GetNews?apikey=YOUR_API_KEY_HERE&return=enriched.url.title,enriched.url.url&start=1446336000&end=1447023600&q.enriched.url.cleanedTitle=seminar&q.enriched.url.enrichedTitle.taxonomy.taxonomy_.label=technology%20and%20computing&count=25&outputMode=json", function(data){
//    debugger;
//    alert(data);
//});

function setup(){
    loadJSON("https://access.alchemyapi.com/calls/data/GetNews?apikey=YOUR_API_KEY_HERE&return=enriched.url.title,enriched.url.url&start=1446336000&end=1447023600&q.enriched.url.cleanedTitle=seminar&q.enriched.url.enrichedTitle.taxonomy.taxonomy_.label=technology%20and%20computing&count=25&outputMode=json", gotData, 'jsonp');
}

function gotData(data){
    println(data);
}
