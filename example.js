var SayAbel  = require('./index.js')
var sayabelInstance = new SayAbel(true);

sayabelInstance.learnFromString("Hello World, How are you? World is big. It is very big. It is not very big");

sayabelInstance.learnFromFile("Hello World, How are you? World is big. It is very big. It is not very big");


sayabelInstance.generateText(10, (text, err) => {
  console.log(text);
});