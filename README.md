# SayAbel
<a href="https://www.npmjs.com/package/sayabel"><img alt="npm version" src="https://img.shields.io/npm/v/sayabel.svg?style=flat-square"></a>
<a href="https://www.npmjs.com/package/sayabel"><img src="https://img.shields.io/npm/dm/syabel.svg?style=flat-square" alt="npm downloads"></a>

## Install
```bash
npm install sayabel
```

## Example Usage
```javascript
var SayAbel  = require('./index.js')
var sayabelInstance = new SayAbel(true);

sayabelInstance.learnFromString("Hello World, How are you? World is big. It is very big. It is not very big");

sayabelInstance.learnFromFile("Hello World, How are you? World is big. It is very big. It is not very big");


sayabelInstance.generateText(10, (text, err) => {
  console.log(text);
});
```
## Documentation

## Main Functionality


