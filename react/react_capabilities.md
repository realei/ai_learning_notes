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

- **React Router Link Tag**

  `import { Link } from 'react-router-dom';`

  `<a></a>`  ----> `<Link></Link>`

  `href` ----> `to`

  **Why do we do that?**

  Well, if you click that link, it's goin to assume that *anchor tag* `<a></a>` is taking you to a whole separate page. And that's not actually really what  we want  to happen. We wanted to actually capture that navigation so the user doesn' reload the React application and then it doesn't unload react.

  Whereas before  it would have reloaded the entire page, now if I click one of these links here, notice  that it doesn't like flash. **It is because it's not reloading  the page all together, React router is now capturing that routing event that navigation event and it's doing the navigation without reloading the application.**


- **Class Components**

  `import { Component } from 'react';`

  `import { withRouter } from 'react-router-dom';`

  **Class Components** have *lifecycle methonds* and they work relatively similar to function components in many ways. But they end up being having  some  slight variations from here to there. And This is like the **original way of writing React**, and **React with hook is a relatively recent thing**, it is only in the past two years(this year is 2021) probably that you've been able to do hooks with react.
