const Discord = require("discord.js-commando"); #requires discord
const bot = new Discord.Client(); #instantiation of client.
#const token = 'REDACTED'; #Discord automatically changed the token because it shouldn't have been uploaded, lesson learned.

bot.on('ready', () =>{
    console.log('BOT BOOTED SUCCESSFULLY') #Console output to prove bot is online.
})

bot.on('message', msg=>{ #message method
    if(msg.content === "+run"){ #Player Typed Command "+run"
        msg.reply('runtest'); #Bot Feedback
        console.log('PLAYER RAN TEST')
    }
    if(msg.content === "+flank"){ #expansion of battle command
        console.log('PLAYER HAS EXPANDED THE FRONTLINE!') #console output
        var sentences = [ #fluff statements
            "The battle has expanded to cover the critical objective of the ",
            "The intensity of the conflict has began to cover the nearby ",
            "Initial telemetry indicates that our fighting elements have moved to cover the critical flank situated the ",
            "Our units have moved to cover positions in the ",
            "Our forces have attempted to create a pivotal counter attack at the ",
            "We have manoevred our forces through the strategically viable position of the ",
            "Advisory units have given field reports that our sponsored forces have taken up positions at the ",
            "In an attempt to assert further control over the battlefield, our forces are moving towards the ",
            "Scattered reports show that fighting has moved to the neighbouring province of ",
            "Our fighters have secured a foothold in the neighbouring provice of "
        ]

        var index = Math.floor(Math.random() * Math.floor(10)) #randomizer for sentences

        var names1 = ["K","G","H","S","Z"]
        var names2 = ["a","e","i","o","u"]
        var names3 = ["g","j","h","s","z"]
        var names4 = ["a","e","i","o","u"]
        var names5 = ["g","q","h","y","z"]
        var names6 = ["a","e","i","o","u"]
        
        var nameindex1 = Math.floor(Math.random() * Math.floor(5)) //randomizer for picking letters in the names.1
        var nameindex2 = Math.floor(Math.random() * Math.floor(5)) //randomizer for picking letters in the names.2
        var nameindex3 = Math.floor(Math.random() * Math.floor(5)) //randomizer for picking letters in the names.3
        var nameindex4 = Math.floor(Math.random() * Math.floor(5)) //randomizer for picking letters in the names.4
        var nameindex5 = Math.floor(Math.random() * Math.floor(5)) //randomizer for picking letters in the names.5
        var nameindex6 = Math.floor(Math.random() * Math.floor(5)) //randomizer for picking letters in the names.6

        var names = names1[nameindex1]+names2[nameindex2]+names3[nameindex3]+names4[nameindex4]+names5[nameindex5]+names6[nameindex6] #concatenating names to make region word.

        var buildings = [ #fluff statements
            "Refinery.",
            "Construction Site.",
            "Factory.",
            "Bunker.",
            "Outpost.",
            "News Station.",
            "Radio Tower.",
            "Airstrip.",
            "Farmlands.",
            "Mine.",
            "Fortifications.",
            "Pipeline.",
            "Strip Mine."
        ]

        var buildingindex = Math.floor(Math.random() * Math.floor(13)) #randomizer for picking letters in the names.


        msg.reply("" + sentences[index] + names + " " + buildings[buildingindex]) 
    }
    if(msg.content === "+march"){ 
        console.log('PLAYER HAS MARCHED')
        var sentences = [
            "Your convoy hit a landmine and has suffered some losses.", 
            "Local scouts have been co-operative and have shown your people a faster route.", 
            "A sandstorm has slowed your movement in the area.",
            "Your forces were subjected to an ambush which they easily repelled, the enemy was poorly equipped and they were repulsed.",
            "Your forces were ambushed! They have taken minor losses and your scouts have reported substantial losses. The main battlegroup remains unhindered.",
            "Your forces manoevred around a fiersome outcropping of warriors, our convoy was shredded.",
            "A dangerous windstorm slowed down progress to the objective, your forces have been delayed."
        ]
        var index = Math.floor(Math.random() * Math.floor(7))
        msg.reply(" " + sentences[index]) 
    }
	
	if(msg.content === "+read"){
		var fs = require('fs');

		fs.readFile('test.csv', 'utf8', function(err, contents) {
			msg.reply("" + contents)
		});
	}
})

bot.login(token); #LOGIN USING TOKEN
