var http = require('http');
var url = require('url');


dummy_feedback={
	"/Q11" : "Right Hand moved.",
	"/Q12" : "Left Hand moved.",
	"/Q13" : "Created C loop around right hand.",
	"/Q14" : "I have picked up needle with right hand.",
	"/Q15" : "I have picked up needle with left hand.",
	"/Q16" : "I have picked up suture with right hand.",
	"/Q17" : "I have pulled suture with both hands to tie a knot."
}

http.createServer(function (req,res){
	res.setHeader('Content-Type','text/html');
	res.writeHead(200, {'Content-Type': 'text/plain'});
 	var q = url.parse(req.url,true);
	content = q.href;
	if (content in dummy_feedback){
		res.end(dummy_feedback[content],'utf-8');}
	else {
		res.end('I do not have any response for that!!','utf-8');
                }
}).listen(8080);

