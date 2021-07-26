# React Capabilities

## React Router Route

[React Router](https://btholt.github.io/complete-intro-to-react-v6/react-router)

The V3, V4 and V5 are wildly different, and they're require rewriting your application can be a bit of a point of frustration. But also by far the best router, it is kinda hard not to use it.

Here we are going to use **React Router 5** today(V6 is coming  now actually).

- **Install React Router**

  `npm install react-router-dom@5.2.0`

  *Conditionally Render*: some time *SearchParams* some time *Details*

  `import { BrowserRouter as Router, Route`` } from 'react-router-dom';`

  **Variables inside your routes:**

  *:id* in below code

  ```
  <router>
	<route path="/details/:id">
	  <searchparams />
	</route>
	<route path="/">
	  <neuralsearch />
	</route>
  </router>
  ```
  
  **Note:**

  - React Router will render all components that the path match.
  - React Router does partial matches. The URL /teachers/jem/young will match the paths /, /teachers, /teachers/jem and /teachers/jem/young. It will not match /young, /jem/young, or /teachers/young.

  **Switch Component**

  This is basically saying, hey, only match one thing,
  only give me the  first one and I don't care about rest of them.

  `import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';`
