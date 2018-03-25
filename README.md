# SayAbel
<a href="https://www.npmjs.com/package/sayabel"><img alt="npm version" src="https://img.shields.io/npm/v/sayabel.svg?style=flat-square"></a>
<a href="https://www.npmjs.com/package/sayabel"><img src="https://img.shields.io/npm/dm/syabel.svg?style=flat-square" alt="npm downloads"></a>

## Install
```bash
npm install sayabel
```

## Example Usage
```javascript
var SayAbel  = require('sayabel')
var sayabelInstance = new SayAbel(true);

sayabelInstance.learnFromFile("data/nietzche-the-joyful-wisdom.txt", (err) => {
  sayabelInstance.generateText(100, (text, err) => {
    console.log(text);
  });
});
```
## Documentation

## Main Functionality


