// const fs = require('fs');
// const puppeteer = require('puppeteer');
// const TurndownService = require('turndown');
// const hljs = require('highlight.js/lib/core');
// const javascript = require('highlight.js/lib/languages/javascript');
// hljs.registerLanguage('javascript', javascript);

// const QUESTIONS_URL =
//   "https://github.com/mauriziomarini/linkedin-skill-assessments-quizzes-1/blob/master/c%2B%2B/c%2B%2Bquiz.md?plain=1";
// const QUESTIONS_PATH = 'src/assets/questions.json';
// const CACHED_QUESTIONS_RAW = fs.readFileSync(QUESTIONS_PATH);
// const CACHED_QUESTIONS = JSON.parse(CACHED_QUESTIONS_RAW);

// (async () => {
//   const browser = await puppeteer.launch();
//   const page = await browser.newPage();
//   await page.goto(QUESTIONS_URL);

//   const questions = await page.evaluate(() => {
//     return getQuestions('h6');

//     function getQuestions(selector) {
//         const rootElement = document.querySelector('.markdown-body');
//         const questionNodes = Array.from(rootElement.querySelectorAll(selector))
//             .filter(({ innerText }) => /^[0-9].+$/.test(innerText));
//         const questions = questionNodes.map((node, index) => ({
//             id: index + 1,
//             title: node.innerText,
//             text: null,
//             code: getCode(node),
//             choices: getChoices(node),
//             answer: getAnswer(node)
//         }));

//         return questions;
//     }
//     function getCode(node) {
//       let code = null;
//       const rootNode = getNextQuestionSibling(node, '.highlight');
//       const codeNode = rootNode && rootNode.querySelector('pre');
//       code = codeNode && codeNode.innerText;

//       // Consider 2 code blocks hack relevant for question #57
//       if (rootNode && rootNode.nextElementSibling.matches('.highlight')) {
//         const codeNode2 = rootNode.nextElementSibling.querySelector('pre');
//         code = `${code}${codeNode2 && `\n\n\n${codeNode2.innerText}`}`;
//       }

//       return code;
//     }
//     function getChoices(node) {
//       const rootNode = getNextQuestionSibling(node, 'ul');
//       const choiceNodes = Array.from(rootNode.querySelectorAll('li'));
//       const choices = choiceNodes.map(node => node.innerHTML);
//       return choices;
//     }
//     function getAnswer(node) {
//       const rootNode = getNextQuestionSibling(node, 'details');
//       const answerNodes = Array.from(rootNode.querySelectorAll(':not(summary)'));
//       const answer = answerNodes.map(node => node.innerHTML).join('');
//       return rootNode.innerHTML;
//       return answer;
//     }
//     function getNextQuestionSibling(element, selector) {
//       let sibling = element.nextElementSibling;

//     	// If there's no selector, return the first sibling
//       if (!selector) return sibling;

//     	// If the sibling matches our selector, use it
//     	// If not, jump to the next sibling and continue the loop
//       while (sibling) {
//         if (sibling.matches(selector)) return sibling;

//         // Exit when we reach the next question selector
//         if (sibling.matches('h6')) break;

//         sibling = sibling.nextElementSibling
//       }
//     }
//   });

//   saveQuestions(questions);

//   await browser.close();
// })();

// function saveQuestions(data) {
//   const turndownService = new TurndownService();
//   const questions = {
//     updatedAt: new Date(),
//     data: data.map(data => {
//       data.code = data.code && hljs.highlight('javascript', data.code).value;
//       data.answer = turndownService.turndown(data.answer).replace('**Answer**\n\n', '');
//       data.choices = data.choices.map(choice => turndownService.turndown(choice));
//       return data;
//     })
//   };

//   // Quick diff before saving
//   if (JSON.stringify(CACHED_QUESTIONS.data) !== JSON.stringify(questions.data)) {
//     fs.writeFile('src/assets/questions.json', JSON.stringify(questions, null, 2), err => {
//       if (err) throw err;
//       console.log('The updated questions.json file has been saved.');
//     });
//   }
//   else {
//     console.log('Nothing to update.');
//   }
// }




















const fs = require("fs");
const puppeteer = require("puppeteer");
const TurndownService = require("turndown");
const hljs = require("highlight.js/lib/core");
const cpp = require("highlight.js/lib/languages/cpp"); // Adjusted for C++ syntax highlighting
hljs.registerLanguage("cpp", cpp);

const QUESTIONS_URL =
  "https://github.com/mauriziomarini/linkedin-skill-assessments-quizzes-1/blob/master/c%2B%2B/c%2B%2Bquiz.md?plain=1";
const QUESTIONS_PATH = "src/assets/questions.json";

// Ensure that the questions.json file exists
if (!fs.existsSync(QUESTIONS_PATH)) {
  fs.writeFileSync(QUESTIONS_PATH, JSON.stringify({ data: [] }, null, 2));
}

const CACHED_QUESTIONS_RAW = fs.readFileSync(QUESTIONS_PATH);
const CACHED_QUESTIONS = JSON.parse(CACHED_QUESTIONS_RAW);

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(QUESTIONS_URL, { waitUntil: "networkidle2" });

  const questions = await page.evaluate(() => {
    const rootElement = document.querySelector(".markdown-body");
    if (!rootElement) {
      throw new Error("Root element with '.markdown-body' not found.");
    }
    return getQuestions("h4");

    function getQuestions(selector) {
      const questionNodes = Array.from(
        rootElement.querySelectorAll(selector)
      ).filter(({ innerText }) => /^Q\d+\..+$/.test(innerText));
      const questions = questionNodes.map((node, index) => ({
        id: index + 1,
        title: node.innerText.trim(),
        text: getText(node),
        code: getCode(node),
        choices: getChoices(node),
        answer: getAnswer(node),
      }));

      return questions;
    }

    function getText(node) {
      const textNode = node.nextElementSibling;
      return textNode && textNode.tagName === "P" ? textNode.innerText : null;
    }

    function getCode(node) {
      let code = null;
      const rootNode = getNextQuestionSibling(node, ".highlight");
      const codeNode = rootNode && rootNode.querySelector("pre");
      code = codeNode && codeNode.innerText;

      // Consider 2 code blocks hack relevant for question #57
      if (
        rootNode &&
        rootNode.nextElementSibling &&
        rootNode.nextElementSibling.matches(".highlight")
      ) {
        const codeNode2 = rootNode.nextElementSibling.querySelector("pre");
        code = `${code}${codeNode2 && `\n\n\n${codeNode2.innerText}`}`;
      }

      return code;
    }

    function getChoices(node) {
      const rootNode = getNextQuestionSibling(node, "ul");
      if (!rootNode) return [];
      const choiceNodes = Array.from(rootNode.querySelectorAll("li"));
      return choiceNodes.map((node) => node.innerText.trim());
    }

    function getAnswer(node) {
      const rootNode = getNextQuestionSibling(node, "p");
      if (!rootNode) return "";
      const answerNode = rootNode.querySelector("strong");
      return answerNode ? answerNode.innerText.trim() : "";
    }

    function getNextQuestionSibling(element, selector) {
      let sibling = element.nextElementSibling;

      // If there's no selector, return the first sibling
      if (!selector) return sibling;

      // If the sibling matches our selector, use it
      // If not, jump to the next sibling and continue the loop
      while (sibling) {
        if (sibling.matches(selector)) return sibling;

        // Exit when we reach the next question selector
        if (sibling.matches("h4")) break;

        sibling = sibling.nextElementSibling;
      }
      return null;
    }
  });

  saveQuestions(questions);

  await browser.close();
})().catch((err) => {
  console.error("An error occurred:", err);
});

function saveQuestions(data) {
  const turndownService = new TurndownService();
  const questions = {
    updatedAt: new Date(),
    data: data.map((data) => {
      data.code = data.code && hljs.highlight("cpp", data.code).value;
      data.answer = turndownService.turndown(data.answer);
      data.choices = data.choices.map((choice) =>
        turndownService.turndown(choice)
      );
      return data;
    }),
  };

  // Quick diff before saving
  if (
    JSON.stringify(CACHED_QUESTIONS.data) !== JSON.stringify(questions.data)
  ) {
    fs.writeFile(
      "src/assets/questions.json",
      JSON.stringify(questions, null, 2),
      (err) => {
        if (err) throw err;
        console.log("The updated questions.json file has been saved.");
      }
    );
  } else {
    console.log("Nothing to update.");
  }
}



