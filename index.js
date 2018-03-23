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
    this.data = {}
};

/**
 * Learn from a plaintext file
 * @param {*} filename file to analyze
 * @param {*} callback function to call when finished
 */
SayAbel.prototype.learnFromFile = function(filename, callback) {
    err = null;

    fs.readFile(filename, 'utf8', (err, contents) => {
        console.log(contents);
    });
    if(callback) {
        callback(err);
    }
};

/**
 * Learn from a string
 * @param {*} string text to analyze
 * @param {*} callback function to call when finished
 */
SayAbel.prototype.learnFromString = function(string, callback) {
    err = null;

    var words = string.split(' ');
    for(i = 0; i < words.length; i++) {
        if(words[i + 1] != null) {
            if(this.data[words[i]] == null) {
                this.data[words[i]] = [];
            }
            this.data[words[i]].push(words[i + 1]);
        }
    }
    if(callback) {
        callback(err);
    }
}

/**
 * Generate text of a given length2
 * @param {*} data data generated
 * @param {*} length approximate word count of returned message.
 * @param {*} callback function to call when finished
 */
SayAbel.prototype.generateText = function(length, callback) {
    err = null;
    response = ["World"];
    for(i = 0; i < length; i++) {
        possibleWords = this.data[response[i]]
        if(possibleWords) {
            response.push(possibleWords[Math.floor(Math.random() * possibleWords.length) + 0]);
        }else {
            response.push(". ");
        }
    }
    if(callback) {
        callback(response, err);
    }
}

//Export our functions as a psuedo-class
module.exports = SayAbel;