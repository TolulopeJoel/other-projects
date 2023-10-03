import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import api, { apiWithoutToken } from "../components/api";
import Navbar from "../components/Navbar";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';


export default function PostDetail() {
    const { postSlug } = useParams();
    const [post, setPost] = useState({ author: {}, comments: [] });

    const [commentBody, setcommentBody] = useState("");

    useEffect(() => {
        apiWithoutToken.get(`/blog/posts/${postSlug}/`)
            .then((response) => {
                setPost(response.data)
            })
            .catch((error) => console.log(error))
    }, [postSlug]);


    const handleSubmit = async (event) => {
        event.preventDefault();
        const postId = post.id;
        try {
            await api.post("/blog/comments/", {
                body: commentBody,
                post_id: postId,
            });
            window.location.reload();
        } catch (error) {
            console.error(error);
        }
    };


    return (
        <>
            <Navbar />
            <div id="content" className="container">
                <div className="row entry-wrap">
                    <div className="column lg-12">

                        <article className="entry format-standard">

                            <header className="entry__header">

                                <h1 className="text-center display-1 font-one mb-3">{post.title}</h1>
                                <div className="mb-5 d-flex justify-content-center">
                                    <div className="p-3">
                                        <svg width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <circle cx="12" cy="8" r="3.25" stroke="currentColor" strokeLinecap="round"
                                                stroke-line-join="round" strokeWidth="1.5"></circle>
                                            <path stroke="currentColor" strokeLinecap="round" stroke-line-join="round"
                                                strokeWidth="1.5"
                                                d="M6.8475 19.25H17.1525C18.2944 19.25 19.174 18.2681 18.6408 17.2584C17.8563 15.7731 16.068 14 12 14C7.93201 14 6.14367 15.7731 5.35924 17.2584C4.82597 18.2681 5.70558 19.25 6.8475 19.25Z">
                                            </path>
                                        </svg>
                                        <a href="">{post.author.first_name} {post.author.last_name}</a>
                                    </div>
                                    <div className="p-3">
                                        <svg width="24" height="24" fill="none" viewBox="0 0 24 24">
                                            <circle cx="12" cy="12" r="7.25" stroke="currentColor" strokeWidth="1.5">
                                            </circle>
                                            <path stroke="currentColor" strokeWidth="1.5" d="M12 8V12L14 14"></path>
                                        </svg>
                                        {new Date(post.published_date).toDateString()}
                                    </div>
                                </div>
                            </header>

                            <div>
                                <figure>
                                    <img src={post.thumbnail}
                                        sizes="(max-width: 2400px) 100vw, 2400px" alt="" />
                                </figure>
                            </div>

                            <div>
                                <div>
                                    <p className="my-5">
                                        {post.body}
                                    </p>
                                    <div className="row">
                                        <figure className="col-lg-2 col-sm-12">
                                            <img alt="" src={post.author.profile_picture} className="avatar" />
                                        </figure>
                                        <div className="col-lg-8 col-sm-12">
                                            <h5>
                                                <a href="#0">
                                                    {post.author.first_name}
                                                </a>
                                            </h5>
                                            <p>
                                                {post.author.bio}
                                            </p>
                                        </div>
                                    </div>

                                </div>

                                <div className="post-nav">
                                    <div className="post-nav__prev">
                                        <a href="single-standard.html" rel="prev">
                                            <span>Prev</span>
                                            The Pomodoro Technique Really Works.
                                        </a>
                                    </div>
                                    <div className="post-nav__next">
                                        <a href="single-standard.html" rel="next">
                                            <span>Next</span>
                                            How Imagery Drives User Experience.
                                        </a>
                                    </div>
                                </div>

                            </div>

                        </article>

                        <div className="comments-wrap">

                            <div id="comments">
                                <div className="large-12">

                                    <h3 className="text-center">{post.comments.length} Comments</h3>
                                    {post.comments && post.comments.map(comment => (

                                        <ul>
                                            <li className="row py-4">
                                                <div className="col-lg-2 col-sm-12 rounded-circle">
                                                    <img className="avatar" src={comment.author.profile_picture} alt="" width="50"
                                                        height="50" />
                                                </div>

                                                <div className="col-sm-12 col-lg-8">
                                                    <div className="pb-2"><b>{comment.author.first_name}</b></div>
                                                    <div className="pb-3">{new Date(comment.created_at).toDateString()}</div>
                                                    <p>{comment.body}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    ))}

                                </div>
                            </div>


                            <div className="comment-respond">

                                <h3 className="text-center">
                                    Add Comment
                                </h3>
                                <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                                    <TextField margin="normal" required rows={10} multiline={true} fullWidth placeholder="Your Message"
                                        type="password" value={commentBody} onChange={(event) => setcommentBody(event.target.value)} />
                                    <input name="submit" id="submit"
                                        className="btn btn-primary w-100 my-4 py-3"
                                        value="Add Comment" type="submit" />
                                </Box>

                            </div>

                        </div>

                    </div>
                </div>
            </div>
        </>
    );
}
