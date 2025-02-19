# 0x15. JavaScript - Web jQuery

## Background Context

This project focuses on using jQuery to manipulate the DOM, handle events, and make AJAX requests. By completing this project, you will gain hands-on experience with jQuery, a fast and concise JavaScript library that simplifies HTML document traversal, event handling, and animation.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Environment**  | Chrome (version 57.0) |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All JavaScript files must end with `.js` |

## General Requirements

1. **Allowed Editors**: vi, vim, emacs
2. **File Structure**: All files should end with a new line.
3. **Code Style**: Your code should be semistandard compliant with the flag `--global $: semistandard *.js --global $`.
4. **JQuery Version**: You must use jQuery version 3.x.
5. **Variables**: You are not allowed to use `var`.
6. **HTML Reload**: HTML should not reload for each action: DOM manipulation, update values, fetch data, etc.

## More Info

### Import JQuery
```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

### Manual QA Review
It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|----------------------------------------------|-------------------------------|
| **0. No JQuery**              | Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) using `document.querySelector` | `0-script.js` |
| **1. With JQuery**            | Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) using the jQuery API | `1-script.js` |
| **2. Click and turn red**     | Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header` using the jQuery API | `2-script.js` |
| **3. Add `.red` class**       | Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header` using the jQuery API | `3-script.js` |
| **4. Toggle classes**         | Write a JavaScript script that toggles the class of the `<header>` element between `red` and `green` when the user clicks on the tag `DIV#toggle_header` using the jQuery API | `4-script.js` |
| **5. List of elements**      | Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item` using the jQuery API | `5-script.js` |
| **6. Change the text**        | Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header` using the jQuery API | `6-script.js` |
| **7. Star wars character**    | Write a JavaScript script that fetches the character name from a URL and displays it in the HTML tag `DIV#character` using the jQuery API | `7-script.js` |
| **8. Star Wars movies**       | Write a JavaScript script that fetches and lists the title for all movies from a URL in the HTML tag `UL#list_movies` using the jQuery API | `8-script.js` |
| **9. Say Hello!**             | Write a JavaScript script that fetches and displays the translation of "Hello" in French in the HTML tag `DIV#hello` using the jQuery API | `9-script.js` |
| **10. No jQuery - document loaded** | Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) using `document.querySelector` and must be imported from the `<head>` tag | `100-script.js` |
| **11. List, add, remove**     | Write a JavaScript script that adds, removes, and clears `<li>` elements from a list when the user clicks on respective buttons using the jQuery API | `101-script.js` |
| **12. Say hello to everybody!** | Write a JavaScript script that fetches and prints how to say “Hello” depending on the language using the jQuery API | `102-script.js` |
| **13. And press ENTER**       | Write a JavaScript script that fetches and prints how to say “Hello” depending on the language when the user clicks on a button or presses ENTER using the jQuery API | `103-script.js` |

## Submission

- **GitHub Repository**: [alx-higher_level_programming](https://github.com/Achrafsadeq/alx-higher_level_programming)
- **Directory**: `0x15-javascript-web_jquery`

## Developer

**Codename**: Achraf Sadeq

## Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.
