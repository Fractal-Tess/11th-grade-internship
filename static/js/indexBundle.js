/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./src/index.ts":
/*!**********************!*\
  !*** ./src/index.ts ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\nconst video = document.getElementById('video');\r\nPromise.all([\r\n    faceapi.nets.tinyFaceDetector.loadFromUri('/static/models'),\r\n    faceapi.nets.faceLandmark68Net.loadFromUri('/static/models'),\r\n    faceapi.nets.faceRecognitionNet.loadFromUri('/static/models'),\r\n    faceapi.nets.faceExpressionNet.loadFromUri('/static/models')\r\n]).then(startVideo).catch(err => console.error(err));\r\nfunction startVideo() {\r\n    navigator.getUserMedia({ video: {} }, stream => video.srcObject = stream, err => console.error(err));\r\n}\r\nvideo.addEventListener('play', () => {\r\n    const canvas = faceapi.createCanvasFromMedia(video);\r\n    document.body.append(canvas);\r\n    const displaySize = { width: video.width, height: video.height };\r\n    faceapi.matchDimensions(canvas, displaySize);\r\n    setInterval(async () => {\r\n        const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions();\r\n        const resizedDetections = faceapi.resizeResults(detections, displaySize);\r\n        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);\r\n        faceapi.draw.drawDetections(canvas, resizedDetections);\r\n        faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);\r\n        faceapi.draw.drawFaceExpressions(canvas, resizedDetections);\r\n    }, 30);\r\n});\r\n\r\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mYWNlcmVjb25nLy4vc3JjL2luZGV4LnRzP2ZmYjQiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IjtBQUVBLE1BQU0sS0FBSyxHQUFHLFFBQVEsQ0FBQyxjQUFjLENBQUMsT0FBTyxDQUFzQjtBQUduRSxPQUFPLENBQUMsR0FBRyxDQUFDO0lBQ1YsT0FBTyxDQUFDLElBQUksQ0FBQyxnQkFBZ0IsQ0FBQyxXQUFXLENBQUMsZ0JBQWdCLENBQUM7SUFDM0QsT0FBTyxDQUFDLElBQUksQ0FBQyxpQkFBaUIsQ0FBQyxXQUFXLENBQUMsZ0JBQWdCLENBQUM7SUFDNUQsT0FBTyxDQUFDLElBQUksQ0FBQyxrQkFBa0IsQ0FBQyxXQUFXLENBQUMsZ0JBQWdCLENBQUM7SUFDN0QsT0FBTyxDQUFDLElBQUksQ0FBQyxpQkFBaUIsQ0FBQyxXQUFXLENBQUMsZ0JBQWdCLENBQUM7Q0FDN0QsQ0FBQyxDQUFDLElBQUksQ0FBQyxVQUFVLENBQUMsQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLEVBQUUsQ0FBQyxPQUFPLENBQUMsS0FBSyxDQUFDLEdBQUcsQ0FBQyxDQUFDO0FBRXBELFNBQVMsVUFBVTtJQUNqQixTQUFTLENBQUMsWUFBWSxDQUNwQixFQUFFLEtBQUssRUFBRSxFQUFFLEVBQUUsRUFDYixNQUFNLENBQUMsRUFBRSxDQUFDLEtBQUssQ0FBQyxTQUFTLEdBQUcsTUFBTSxFQUNsQyxHQUFHLENBQUMsRUFBRSxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLENBQzFCO0FBQ0gsQ0FBQztBQUVELEtBQUssQ0FBQyxnQkFBZ0IsQ0FBQyxNQUFNLEVBQUUsR0FBRyxFQUFFO0lBQ2xDLE1BQU0sTUFBTSxHQUFHLE9BQU8sQ0FBQyxxQkFBcUIsQ0FBQyxLQUFLLENBQUM7SUFDbkQsUUFBUSxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsTUFBTSxDQUFDO0lBQzVCLE1BQU0sV0FBVyxHQUFHLEVBQUUsS0FBSyxFQUFFLEtBQUssQ0FBQyxLQUFLLEVBQUUsTUFBTSxFQUFFLEtBQUssQ0FBQyxNQUFNLEVBQUU7SUFDaEUsT0FBTyxDQUFDLGVBQWUsQ0FBQyxNQUFNLEVBQUUsV0FBVyxDQUFDO0lBQzVDLFdBQVcsQ0FBQyxLQUFLLElBQUksRUFBRTtRQUNyQixNQUFNLFVBQVUsR0FBRyxNQUFNLE9BQU8sQ0FBQyxjQUFjLENBQUMsS0FBSyxFQUFFLElBQUksT0FBTyxDQUFDLHVCQUF1QixFQUFFLENBQUMsQ0FBQyxpQkFBaUIsRUFBRSxDQUFDLG1CQUFtQixFQUFFO1FBQ3ZJLE1BQU0saUJBQWlCLEdBQUcsT0FBTyxDQUFDLGFBQWEsQ0FBQyxVQUFVLEVBQUUsV0FBVyxDQUFDO1FBQ3hFLE1BQU0sQ0FBQyxVQUFVLENBQUMsSUFBSSxDQUFDLENBQUMsU0FBUyxDQUFDLENBQUMsRUFBRSxDQUFDLEVBQUUsTUFBTSxDQUFDLEtBQUssRUFBRSxNQUFNLENBQUMsTUFBTSxDQUFDO1FBQ3BFLE9BQU8sQ0FBQyxJQUFJLENBQUMsY0FBYyxDQUFDLE1BQU0sRUFBRSxpQkFBaUIsQ0FBQztRQUN0RCxPQUFPLENBQUMsSUFBSSxDQUFDLGlCQUFpQixDQUFDLE1BQU0sRUFBRSxpQkFBaUIsQ0FBQztRQUN6RCxPQUFPLENBQUMsSUFBSSxDQUFDLG1CQUFtQixDQUFDLE1BQU0sRUFBRSxpQkFBaUIsQ0FBQztJQUM3RCxDQUFDLEVBQUUsRUFBRSxDQUFDO0FBQ1IsQ0FBQyxDQUFDIiwiZmlsZSI6Ii4vc3JjL2luZGV4LnRzLmpzIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgUHJlZGljdEFsbEZhY2VFeHByZXNzaW9uc1dpdGhGYWNlQWxpZ25tZW50VGFzayB9IGZyb20gXCIuLi9ub2RlX21vZHVsZXMvZmFjZS1hcGkuanMvYnVpbGQvY29tbW9uanMvZ2xvYmFsQXBpL1ByZWRpY3RGYWNlRXhwcmVzc2lvbnNUYXNrXCJcclxuXHJcbmNvbnN0IHZpZGVvID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3ZpZGVvJykhIGFzIEhUTUxWaWRlb0VsZW1lbnRcclxuXHJcblxyXG5Qcm9taXNlLmFsbChbXHJcbiAgZmFjZWFwaS5uZXRzLnRpbnlGYWNlRGV0ZWN0b3IubG9hZEZyb21VcmkoJy9zdGF0aWMvbW9kZWxzJyksXHJcbiAgZmFjZWFwaS5uZXRzLmZhY2VMYW5kbWFyazY4TmV0LmxvYWRGcm9tVXJpKCcvc3RhdGljL21vZGVscycpLFxyXG4gIGZhY2VhcGkubmV0cy5mYWNlUmVjb2duaXRpb25OZXQubG9hZEZyb21VcmkoJy9zdGF0aWMvbW9kZWxzJyksXHJcbiAgZmFjZWFwaS5uZXRzLmZhY2VFeHByZXNzaW9uTmV0LmxvYWRGcm9tVXJpKCcvc3RhdGljL21vZGVscycpXHJcbl0pLnRoZW4oc3RhcnRWaWRlbykuY2F0Y2goZXJyID0+IGNvbnNvbGUuZXJyb3IoZXJyKSlcclxuXHJcbmZ1bmN0aW9uIHN0YXJ0VmlkZW8oKSB7XHJcbiAgbmF2aWdhdG9yLmdldFVzZXJNZWRpYShcclxuICAgIHsgdmlkZW86IHt9IH0sXHJcbiAgICBzdHJlYW0gPT4gdmlkZW8uc3JjT2JqZWN0ID0gc3RyZWFtLFxyXG4gICAgZXJyID0+IGNvbnNvbGUuZXJyb3IoZXJyKVxyXG4gIClcclxufVxyXG5cclxudmlkZW8uYWRkRXZlbnRMaXN0ZW5lcigncGxheScsICgpID0+IHtcclxuICBjb25zdCBjYW52YXMgPSBmYWNlYXBpLmNyZWF0ZUNhbnZhc0Zyb21NZWRpYSh2aWRlbylcclxuICBkb2N1bWVudC5ib2R5LmFwcGVuZChjYW52YXMpXHJcbiAgY29uc3QgZGlzcGxheVNpemUgPSB7IHdpZHRoOiB2aWRlby53aWR0aCwgaGVpZ2h0OiB2aWRlby5oZWlnaHQgfVxyXG4gIGZhY2VhcGkubWF0Y2hEaW1lbnNpb25zKGNhbnZhcywgZGlzcGxheVNpemUpXHJcbiAgc2V0SW50ZXJ2YWwoYXN5bmMgKCkgPT4ge1xyXG4gICAgY29uc3QgZGV0ZWN0aW9ucyA9IGF3YWl0IGZhY2VhcGkuZGV0ZWN0QWxsRmFjZXModmlkZW8sIG5ldyBmYWNlYXBpLlRpbnlGYWNlRGV0ZWN0b3JPcHRpb25zKCkpLndpdGhGYWNlTGFuZG1hcmtzKCkud2l0aEZhY2VFeHByZXNzaW9ucygpXHJcbiAgICBjb25zdCByZXNpemVkRGV0ZWN0aW9ucyA9IGZhY2VhcGkucmVzaXplUmVzdWx0cyhkZXRlY3Rpb25zLCBkaXNwbGF5U2l6ZSlcclxuICAgIGNhbnZhcy5nZXRDb250ZXh0KCcyZCcpLmNsZWFyUmVjdCgwLCAwLCBjYW52YXMud2lkdGgsIGNhbnZhcy5oZWlnaHQpXHJcbiAgICBmYWNlYXBpLmRyYXcuZHJhd0RldGVjdGlvbnMoY2FudmFzLCByZXNpemVkRGV0ZWN0aW9ucylcclxuICAgIGZhY2VhcGkuZHJhdy5kcmF3RmFjZUxhbmRtYXJrcyhjYW52YXMsIHJlc2l6ZWREZXRlY3Rpb25zKVxyXG4gICAgZmFjZWFwaS5kcmF3LmRyYXdGYWNlRXhwcmVzc2lvbnMoY2FudmFzLCByZXNpemVkRGV0ZWN0aW9ucylcclxuICB9LCAzMClcclxufSkiXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/index.ts\n");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The require scope
/******/ 	var __webpack_require__ = {};
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval-source-map devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/index.ts"](0, __webpack_exports__, __webpack_require__);
/******/ 	
/******/ })()
;