// Set of utility functions to make index.js easier to test

function getButtonById(id) {
    return document.getElementById(id);
  }
  
  function getBodyScrollTop() {
    return document.body.scrollTop;
  }
  
  function getDocumentElementScrollTop() {
    return document.documentElement.scrollTop;
  }
  
  module.exports = { getButtonById, getBodyScrollTop, getDocumentElementScrollTop };
  