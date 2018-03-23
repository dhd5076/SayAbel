/**
 * Main functions for text analysis and text generation
 */
"use scrict";
const fs = require('fs');

/**
 * Creates a new SayAbel instance
 * @param {*} debug whether to output debug information
 * @param {*} callback functionn to call when finished
 */
function SayAbel(debug, callback) {
    this.debug = debug;
};

/**
 * Learn from a plaintext file
 * @param {*} filename file to analyze
 * @param {*} callback function to call when finished
 */
SayAbel.prototype.learnFromFile = function(filename, callback) {
    err = null;
    callback(err);
};

/**
 * Learn from a string
 * @param {*} string text to analyze
 * @param {*} callback function to call when finished
 */
SayAbel.prototype.learnFromString = function(string, callback) {
    err = null;
    data = {};

    var words = string.split(' ');
    for(i = 0; i < words.length; i++) {
        if(words[i + 1] != null) {
            if(data[words[i]] == null) {
                data[words[i]] = [];
            }
            data[words[i]].push(words[i + 1]);
        }
    }
    callback(data, err);
}

/**
 * 
 * @param {*} data data generated
 * @param {*} length approximate word count of returned message.
 * @param {*} callback function to call when finished
 */
SayAbel.prototype.generateText = function(wordlist, length, callback) {
    err = null;
    response = ["is"];
    for(i = 0; i < length; i++) {
        response += wordlist[0]
    }
    callback(data, err)
}

//Export our functions as a psuedo-class
module.exports = SayAbel;