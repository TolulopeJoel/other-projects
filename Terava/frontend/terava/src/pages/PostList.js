import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Pagination from "../components/Pagination";
import { apiWithoutToken } from "../components/api";
import '../assets/css/styles.css';


function PostList() {
  const [next, setNext] = useState();
  const [posts, setPosts] = useState([]);
  const [count, setCount] = useState();
  const [previous, setPrevious] = useState();
  const [prascal, SetPrascal] = useState({});

  useEffect(() => {
    apiWithoutToken.get('/blog/posts/')
      .then((response) => {
        setPosts(response.data.results);
        setNext(response.data.next);
        setPrevious(response.data.previous);
        setCount(response.data.count);
      }).catch(error => console.log(error));
  }, []);

  return (
    <>
      <div className="er-container">
        <div className="gallery-container">
          {posts && posts.map(post => (
            <figure>
              <a href={`/blog/${post.slug}/`}><img src={post.thumbnail} alt="" /></a>
              <figcaption className="py-5">
                <span className="bottle"><b>BY</b>: {post.author.first_name} {post.author.last_name}</span>
                <h2 className="post-list-title "><a href={`/blog/${post.slug}/`}>{post.title}</a></h2>
                <p className="mb-4">{post.summary_body}</p>
                <a href={`/blog/${post.slug}/`} className="read-more-btn">READ MORE</a>
              </figcaption>
            </figure>
          ))}
        </div>
      </div>
    </>
  );
}

export default PostList;