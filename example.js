var SayAbel  = require('./index.js')
var sayabelInstance = new SayAbel(true);

sayabelInstance.learnFromFile("data/plato-phaedrus-clean.txt", (err) => {
  sayabelInstance.generateText(10, (text, err) => {
    console.log(text);
  });
});