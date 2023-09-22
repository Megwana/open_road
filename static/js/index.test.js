// Mocking the DOM element:
const mockButton = {
    style: {}
};

// Mocking document methods:
document.getElementById = jest.fn().mockReturnValue(mockButton);
document.body.scrollTop = 0;
document.documentElement.scrollTop = 0;

// Importing the functions from the module:
const { scrollFunction, topFunction } = require('./index');

test('scrollFunction should hide button if scrollTop <= 10', () => {
  document.body.scrollTop = 5;
  document.documentElement.scrollTop = 5;

  scrollFunction();

  expect(mockButton.style.display).toBe('none');
});

test('scrollFunction should display button if scrollTop > 10', () => {
  document.body.scrollTop = 15;
  document.documentElement.scrollTop = 15;

  scrollFunction();

  expect(mockButton.style.display).toBe('block');
});

test('topFunction should reset scrollTop to 0', () => {
  topFunction();

  expect(document.body.scrollTop).toBe(0);
  expect(document.documentElement.scrollTop).toBe(0);
});