var SlackBot = require('slackbot');
var Client = require('node-rest-client').Client;

var bot = new SlackBot({
    token: '<here>',
    name: 'traffic'
});

bot.on('start', function() {
    params = {
        icon_emojo: ':ghost:'
    }
});

bot.on('message', function(data) {
    console.log(data);
    console.log('----------------');
});