var SayAbel  = require('./index.js')
var sayabelInstance = new SayAbel(true);

sayabelInstance.learnFromFile("data/nietzsche-the-joyful-wisdom.txt", (err) => {
  sayabelInstance.generateText(100, (text, err) => {
    console.log(text);
  });
});