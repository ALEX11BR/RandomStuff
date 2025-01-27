// ==UserScript==
// @name        New script upb.ro
// @namespace   Violentmonkey Scripts
// @match       https://curs.upb.ro/*
// @grant       none
// @version     1.0
// @author      -
// @description 12/22/2024, 4:46:39 AM
// ==/UserScript==
document.querySelectorAll("a").forEach(el => {
  el.href = el.href.replace(/\?forcedownload=1$/, "")
})