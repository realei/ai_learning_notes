# Special Case React Tools

## Error Boundaries

*This is one of the features that only Class Components can do. You literally can not do these in Function Components, so **if you need something that has error boundaries, you must use class components**.*

What is React's *[Error Boundaries](https://zh-hans.reactjs.org/docs/error-boundaries.html)*

- `componentDidMatch()` --- a lifecycle method

  This is really useful if you expect errors coming from within your application.

  I can say, if there's an  error somewhere in here, dont't crash my application, just go ahead and catch it and then do something with it. So something I've seen apps do is I'll put one error boundary at the *very top level*, so they're like, hey, *if  an error happens anywhere in here, let's recover, let's send the user back to a good state*, let's just not crash the application altogether.

  I actually find these really useful with APIs, especially if that  API is unreliable.

  **Error Mornitoring Services:* Sentry, Azure Monitor, New Relic, TrackJS

## Redirect on Error

  `import Redirect from 'react-router-dom';`

- `componentDidUpdate()` --- A lifecycle method, this gets called anytime that the component updates itself. 

  **Note:** `componentDidUpdate()` can not be called on the very first time that it renders whichi you would assume that you wouldn't hit an error on the first time.

## Context

  So we are heading back to hooks, we spent a bunch of time on Class Components. Let's go back to use some hooks now.

  **Note:** "context" is a *sledgehammer(大锤)*, so dont use it all the time. You will *muddy浑 up* your code and make things less obvious which is the *React's big advantange  here is that the codes very obvious when you read it*.

  ```
  // ThemeContext.js
  import { createContext } from 'react';

  const ThemeContext = createContext();

  export default ThemeContext;
  ```
  The default value that we're going to give it is actually going to be a hook. We are going to use context and  hooks together.

  **prop Drilling钻孔**, we have to prop pass it from parent to child parent to child until it  eventually get to the the place you want to. That kind of the things that context psalteries诗篇 the prop drilling.

## Implementing ThemeContext and Q&A

  We are going  to make `SearchParams` be able to change what the theme is. 

  There is a *hook** called `useContext`
 
  ```
  import { useState, useEffect, useContext } from "react";
  import ThemeContext from "./ThemeContext";

  // Here is the fun part
  const [theme] = useContext(ThemeContext)
  ```

  I now  have accessto the theme that's available everywherer my application. I am just able to *yank 猛拉* it out of context. This didn't come from props, this didn't come from state or anything like that, it came from the  context.

  `<button style={{ backgroundColor: theme }}>Submit</button>`

  Above has two *curly brace {}*, one is a signifying to react or to JSX I'm about to give you a JavaScript expression; and inside of that I have an object. That's what the couble curly braces, it's actually two separate sets, it's not that they mean anything together.

  **What context is?** Now there's this universally available context that I can access anywhere my application.

  **Q1:** So is the returned value for `ThemeContext` or from `context` in general,the  same  as hook?

  *Answer:* Not necessarily, let's go back and look at `App.js`

  ```
  const App = () => {
  const [theme] = useState("darkblue");
  return (
    <ThemeContext.Provider value={theme}>
      <div>
        <Router>
          <header>
            <Link to="/">
              <h1>AI Search</h1>
            </Link>
          </header>

          <Switch>
            <Route path="/details/:id">
              {/*
              Passing these theme properties from component to component to component.
              This is called prop drilling, we have to prop pass it from parent to child.
              */}
              <Details theme={theme}/>
            </Route>
            <Route path="/">
              <NeuralSearch />
            </Route>
          </Switch>
        </Router>
      </div>
    </ThemeContext.Provider>
  );
};

  ```
  What an I putting into `ThemeContext.Provider`, `theme`, what  is `theme`? `theme` is what returned  from `useState`. So it is  literally what's coming out `useState("darkblue")`; **But** lets say I had `const theme = 'green'` and replace the `seState("darkblue")`, it would be green! It's  basically you can think of context basically as like a *wormhole虫洞*, that just connects two different points in your application. Whatever you throw in one side, it's gonna come out the  other side, whatever you  put in is what you're gonna get out.

  **Q2:** When you actually invoke `useContext` in `searchParams.js`, what does that return?
  *Answer:* Whatever you put in. Whatever you put in the `theme` of `App.js` is going  to come out `theme` in `const [theme] = useContext(ThemeContext)` of `SearchParams.js`. **Because** it is a hook at `SearchParams.js` side, it's gonna be a hook on it is  gonna be a hood at this side(`SearchParams.js`); **But**, if it was  an object on one side, it'd be an object on the orther side.

  **Q3:** Can you have multiple contexts?
  *Answer:* Absolutely, you can go in, let's just looks at `App.js`(check it in Q2). I could have multiple layers of context here. I could have one context that *encapsulates* a whole thing kind of like Redux. You actually already have some context  in your application, *because **react router** is using  context extensively广泛地*. That's  how  links  and stuff work, because it's all reading stuff of context.
  
  **Q4:** Another thing you could know but you don't really need to: is **I can have multiple theme contexts**. So if I wrapped details on one of the `SearchParameters.js` in a different one, I could give one pink andone orange, and  it would read from those. *I have never use  that  in production, it  is a nifty party trick漂亮的派对把戏. But you can have multiple layers there, infinite layers I suppose. Yeah, **file that under never used**.*

- Add a **Theme Selector**

  Make a *dropdown* in `SearchParams.js`

  ```
  const [theme, setTheme] = useContext(ThemeContext)
  			.
			.
			.
  {/* make a drop down for "theme" */}V
  <label htmlFor="theme">
    Theme
    <select
	  value={theme}
      onChange={e => setTheme(e.target.value)}
  	  onBlur={e => setTheme(e.target.value)}
	>
	  <option value="darkblue">Dark Blue</option>
	  <option value="peru">Peru</option>
	  <option value="chartreuse">Chartreuse</option>
	  <option value="mediumorchid">Medium Orchide</option>
    </select>
  </label>
  <button style={{ backgroundColor: theme }}>Submit</button>
  
  ```

  So now what we would except is I can change the theme. I'm gonna change the button, that's fine on the same page, I could have done that with `useState` **but** I am also gonna changethe color of the button on `Details` page. **Why is that?** Let's think about where that `state` actually lives. 

  In `App.js`, the `theme` lives above `<Searchparams />`, so even when it  gets unrendered, it gets unrendered from `<Searchparams />`. This state ''theme` fro line `const theme = useState("darkblue")` never went away, so it still set to whatever it was set to here in `<Searchparams />`, **and it's doing that through context. Despite the fact that there is no explicit明确的 connection between `const theme = useState("darkblue")` and `<Searchparams />`, it's using  that *wormhole* of context to go from one place to another.
