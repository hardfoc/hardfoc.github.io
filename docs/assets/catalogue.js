// Repository catalogue filter: the search field and the topic chips hide the cards (and empty groups) that do not
// match. Works with Material's instant navigation (document$), and leaves every card visible without JavaScript.
(function () {
  function setup() {
    var input = document.getElementById("hf-repo-filter");
    if (!input || input.dataset.ready) return;
    input.dataset.ready = "1";
    var cards = Array.prototype.slice.call(document.querySelectorAll(".hf-repo"));
    var groups = Array.prototype.slice.call(document.querySelectorAll(".hf-catalogue__group"));
    var count = document.querySelector(".hf-catalogue__count");
    var total = count ? count.getAttribute("data-total") : String(cards.length);
    var topic = "";

    function apply() {
      var words = input.value.toLowerCase().split(/\s+/).filter(Boolean);
      var shown = 0;
      cards.forEach(function (c) {
        var hay = c.getAttribute("data-search");
        var topics = " " + c.getAttribute("data-topics") + " ";
        var ok = words.every(function (w) { return hay.indexOf(w) !== -1; }) &&
                 (!topic || topics.indexOf(" " + topic + " ") !== -1);
        c.hidden = !ok;
        if (ok) shown++;
      });
      groups.forEach(function (g) { g.hidden = !g.querySelector(".hf-repo:not([hidden])"); });
      document.querySelectorAll(".hf-chipbtn").forEach(function (b) {
        b.setAttribute("aria-pressed", b.getAttribute("data-topic") === topic ? "true" : "false");
      });
      if (count) {
        count.textContent = shown === Number(total) ? total + " public repositories." :
          shown + " of " + total + " repositories" + (topic ? " with topic " + topic : "") + ".";
      }
    }

    input.addEventListener("input", apply);
    document.addEventListener("click", function (e) {
      var b = e.target.closest && e.target.closest(".hf-chipbtn");
      if (!b) return;
      var t = b.getAttribute("data-topic");
      topic = topic === t ? "" : t;
      apply();
    });
    var q = new URLSearchParams(location.search);
    if (q.get("q")) input.value = q.get("q");
    if (q.get("topic")) topic = q.get("topic");
    apply();
  }
  if (window.document$) window.document$.subscribe(setup); else document.addEventListener("DOMContentLoaded", setup);
})();
