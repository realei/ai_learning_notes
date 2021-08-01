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

## Portals, Refs, and Q&A

  Models are terrible user interfaceexperiences, but we still use them everywhere because we haven't discovered a better way as developers to inform users that something is happening.

- Portals

  1. edit `index.html`

  Add 'modal' above 'root':

  ```
  <body>
    <div id="modal"></div>
    <div id="root">Not rendered</div>
    <script src="App.js"></script>
  </body>
  ```

  So now we can render outside above `root` objectively, because `root` is still limited to `<div id="root">Not rendered</div>` and then we can render somethings into `model` when we need to. So it's another like render point.

  2. edit new file `Modal.js`

  `import { useEffect, useRef } from 'react';`

  code:

  ```
  // Modal.js
  import { useEffect, useRef } from 'react';
  import { createPortal } 'react-dom';

  // What we're going to render into
  const modalRoot = document.getElementById('modal');

  const Modal = ({ children }) => {
    const elRef = useRef(null);
    if (!elRef.current) {
      elRef.current = document.createElement('div');
    }

    useEffect(() => {
      // We are going  to append below to the dom
      modalRoot.appendChild(elRef.current);

      // We also need to clean up, after we're done(this is how you clean up an effect)
      return () => modalRoot.removeChild(elRef.current);
    }, []);

	return createPortal(<div>{children}</div>, elRef.current);
  }

  export default Modal;
  ```

  So basically what  we're saying here is, hey, whenever you get created, insert it to the dom; whenever you are done, remove me from dom. And **this prevents memory leaks**, otherwise you'd be leaking `div`s every single time that you created a modal and then unrendered a mondal.

  `retrun` of `Modal.js`: We are goint to wrap this in a `div`, I know it is a bit of *modal soup* or a *div soup*. But the reason being is that sometimes children can be like a list of elements, and top level elements always have to be a single thing. You can use fragments in other places, and we'll talk about fragments later. **But now, trust me put a `div` here, it will make your life easier.**, otherwise you'll get some  random errors sometimes.

  `export default Modal;` Now, we can use this modal anywhere taht we want to, this is now **a reusable  moday  component**.

- Refs

 `useRef`

 In the code `elRef` or `Ref` is  a container for `state` tht you want to survive pass render cycles. So for example, we have this `elRef.current = document.createElment('div');`, we only want one `<div>` and we don't want to create a new `div` on every render. We want to have exactly one `div` all the time.
 
 So if you want to have like some piece of state that you want exactly one instead of a component, you  can use  these things called `Refs`.

 - Q&A

   **Q1:** What happens if we havemultiple models at the same  time?

   *Answer:* You're not always going to use portals for that reason, like imagine if you had a portal that renders to a sidebar and another renders to  the  bottom bar and those kinds of different places. Those could have multiple different containers that they'd be referencing. But if you hvae a  global variable like `const container = document.createElement("div")`, they are all going  to be referencing the same 'div', and that's not actually what you want. You want **each modal to be totally self-contained, right?** So that I can have on each, portal as it were all right! You want each portal be totally contained, right! So this makes it unique per instance of modal. Which is  *why you need to use a ref* so that each one has it's own. Which is pretty great. But now we can render  modals wheneverwe need to, from any part of our application. Kind of an advanced use case,but *suffice to say 足以说* if that didn't make any senseto just trust me until you understand that.

   **Q2:** Do all the refs need to be cleaned up?

   *Answer:* Nope, just ones that need to be cleaned up. So for example above code, these code gets appended to the dom. So even though I stopped referencing it, it still gonna be in the dom. So the dom is holding onto it. **So not every reference has to be cleaned up, but everything from the dom that gets appended the dom does have to be cleaned up.**

   **Q3:** Can you clarify a bit more on what he create role is doing?
   *Answer:* It's rendering out to the dom at that location, and  **Why not use React dom that same in App.js? So like you can't use the same thing again like ``React.dom.render()` as well?** No, because you're rendering basically outside of itself, right? In other words, it might have been able to overload it but it will confusing, so they created two separate methods for it.

 ## Implementing Modals

 check the code please
