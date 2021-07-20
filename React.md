# React Learn by Doing

## File Upload

[React中的文件上传](https://segmentfault.com/a/1190000016824949)

**Three methonds of file upload**:

- form

  *Pros:*

  No need to worry *cros*, click [cros](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS) to learn mor about this topic

  *Cons:*

  by default, form will redirect.

- fetch(or use axios)
  
  *fetch* is browser's native API, it is better use native method 'fetch' when 'axios' is not necessary. But 'fetch' is based on *Promise*, so the browser has to support *Promise*.

- form + fetch
