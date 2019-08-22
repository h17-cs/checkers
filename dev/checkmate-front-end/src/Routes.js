import React from "react";
import { Router, Route, Link, Switch } from 'react-router-dom';
import Home from './containers/Home'
import Login from "./containers/Login";
import Register from "./Register";
import Game from "./components/Game";
import AppliedRoute from "./components/AppliedRoute";


export default ({childProps}) =>
  <Switch>
    <AppliedRoute path="/" exact component={Home} props={childProps}/>
    <Route path="/login" exact component={Login} props={childProps}/>
    <Route path="/register" exact component={Register} props={childProps}/>
    <Route path="/game" exact component={Game} props={childProps}/>
  </Switch>;