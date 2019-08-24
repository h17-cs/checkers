import React from "react";
import { Router, Route, Link, Switch } from 'react-router-dom';
import Home from './containers/Home'
import Login from "./containers/Login";
import Register from "./Register";
import Game from "./components/Game";
import AppliedRoute from "./components/AppliedRoute";
import Chat from "./components/Chat/Chat"


export default ({childProps}) =>
  <Switch>
    <AppliedRoute path="/" exact component={Home} props={childProps}/>
    <AppliedRoute path="/login" exact component={Login} props={childProps}/>
    <Route path="/register" exact component={Register} props={childProps}/>
    <Route path="/game" exact component={Game} props={childProps}/>
    <Route path="/chat" exact component={Chat} props={childProps}/>
  </Switch>;