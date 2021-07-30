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

  
