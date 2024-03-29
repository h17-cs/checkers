import React from "react";
import { Router, Route, Link, Switch } from 'react-router-dom';
import Home from './containers/Home'
import Login from "./containers/Login";
import Register from "./Register";
import Game from "./components/Game";
import AppliedRoute from "./components/AppliedRoute";
import Chat from "./components/Chat/Chat";
import About from "./components/About";


export default ({childProps}) =>
  <Switch>
    <AppliedRoute path="/" exact component={Home} props={childProps}/>
    <AppliedRoute path="/login" component={Login} props={childProps}/>
    <Route path="/register" exact component={Register} props={childProps}/>
    <Route path="/game" render={(props) => <Game username={childProps.username}/>}/>
    <Route path="/chat" exact component={Chat} props={childProps}/>
    <Route path="/about" exact component={About} props={childProps}/>
  </Switch>;