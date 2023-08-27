browser.webNavigation.onHistoryStateUpdated.addListener(function (details) {
  browser.tabs.executeScript(null, { file: "YTMusic.js" });
});
