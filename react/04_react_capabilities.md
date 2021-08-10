# React Capabilities

## React Router Route

[React Router at "btholt"](https://btholt.github.io/complete-intro-to-react-v6/react-router)

[React Router](https://reactrouter.com/web/example/basic)

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

## React Router Link Tag

- Import

  `import { Link } from 'react-router-dom';`

  `<a></a>`  ----> `<Link></Link>`

  `href` ----> `to`

  **Why do we do that?**

  Well, if you click that link, it's goin to assume that *anchor tag* `<a></a>` is taking you to a whole separate page. And that's not actually really what  we want  to happen. We wanted to actually capture that navigation so the user doesn' reload the React application and then it doesn't unload react.

  Whereas before  it would have reloaded the entire page, now if I click one of these links here, notice  that it doesn't like flash. **It is because it's not reloading  the page all together, React router is now capturing that routing event that navigation event and it's doing the navigation without reloading the application.**


## Class Components

- Import & Class Component Metods

  `import { Component } from 'react';`

  `import { withRouter } from 'react-router-dom';`

  **Class Components** have *lifecycle methonds* and they work relatively similar to function components in many ways. But they end up being having  some  slight variations from here to there. And This is like the **original way of writing React**, and **React with hook is a relatively recent thing**, it is only in the past two years(this year is 2021) probably that you've been able to do hooks with react.

  1st should  always be  *render ()* method

  **Function Component** vs **Class Component**
  
  The general React populist  likes *function components* and *hooks* and all that kind  of stuff.

- How do we create **state**?

  Instead of having *hooks* we  have  **individual pieces of state**. With *Class Components*, you actually have **a state object** that you're gonna refer to.

  ```
  class Details extends Component {
    constructor () {
      super();

	  this.sate = { loading: true }
    }
	async componentDidMount () {
      const res = await fetch(
        `http://pets-v2.dev-apis.com/pets?id=${this.props.match.params.id}`
      )
    }
	render() {
	  return <h2>Hi! AI Search!<h2>
	}
  }
  ```

  **1st thing you need to do is call `super();`** inside a *class component constructor*. Because you actually have to call *Component constructor*.

- **life cycle methods**:
  
  -**componentDidMount()**

    `comopnentDidMount()` is the thing that get called as soon as the **React component is rendered for the first time**. So as soon as someone goes to `/details/1`, it's going to render this for the first time and then it's gonna call `componentDidMount()`. This is kind of like the **effect**......, **this is gonna get called once when it's first created and then it's not called again**.

	`http://pets-v2.dev-apis.com/pets?id=${this.props.match.params.id}`

	`this` refer to the detail component

	`props` this  is what has been passed down from the parent

	**`match.params`** is coming from **React Router**. `match` is the *matched path*, the *params* or the parameters that I am getting from the user, and the `id` is whatever I called inside the `<Route>`. 

	```
	<Route path="/details/:id">
      <Details />
    </Route>
	```

  **Note:** If this is a *Function Component*, we can actually use a *special hook* that gets it(`http://pets-v2.dev-apis.com/pets?id=${this.props.match.params.id}`) for you.

  **Note:** By default, *React Router* doesn't pass in all it's information the the `<Details>` component, and to solve this proble: wrap `Detail` with `()` export at the end `export default withRouter(Details);`. And this is just gonna now pass those props in. This is what again, called a **higher order component**.

## Loading State & Lifecycle

- **Life Cycle Methods**
  
  - `componentDidMount()`  --- check above

  ```
  if (this.state.loading) {
    return <h2>Loading...</h2>
  }
  ```

  [React Lifecycle Methods Diagram](https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)

  [Please check React official website](https://zh-hans.reactjs.org/)

  **Q1:** Our class components they **only  way to get  life cycle components**?

  *Answer:* Yes, mostly, but you can use `useEffect()` hook to approcimate/basically get all the life cycle methods.
  There is  only a few that 'Class Component' don't handel, one of them is *Error Boundaries*. So there is a very slight few of things you can only do with 'Class Component', but for the most part, you can do anything with either type.

## Class Properties

  We're gonna do something with our 'Class Component' to make it a lot easier to write.

  - Install
  
  `npm i -D @babel/plugin-proposal-class-properties@7.13.0 @babel/preset-env@7.13.5 @babel/eslint-parser@7.13.4`

  - Configure `.babelrc`

  `"@babel/preset-env"`  ~~ This is what transpires like futuristic JavaScript to previous  JavaScript. 

  *Note:* **Preset** is a group of plugins, and **a plugin** is *just one transform*

  - Configure `.eslintrc.json`

  `"parser": "@babel/eslint-parser",` ~~ This is going to tell ESlint that "before you read any of the code run it through Babbel first".

## Manage State in a Class Component

  **Note:** Whenever Parcel gets in a bad state, just do `rm -rf .cache dist`
  Just remove these  two folders which are generated by Parcel, and then just  run the  server again

  Please check `Carousel.js`

  ```
    import { Component } from 'react';

	class Carousel extends Component {
	  state = {
		active: 0;
	  }

	  static defaultProps = {
		images: ['http://pets-images.dev-apis.com/pets/none.jpg']
	  }

	  render () {
		const { active } = this.state;
		const { images } = this.props;
	  }
	}
  ```

  **this.state** is *mutable*, it's what you  use hooks for previously. And **mutable** is just a really fancy way of saying that this  is changeable.

  **this.props** is what's coming  from my parents, and it is one-way data flow & read-only; 'I' can not change props, only the parents can change props.

## Interactive Class Component

  We will add *event hanglers* here. 

  `handleIndexClick(event)`
