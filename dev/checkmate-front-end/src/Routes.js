import React from "react";
import { Router, Route, Link, Switch } from 'react-router-dom';
import Home from './Home'
import Login from "./Login";
import Register from "./Register";
import Game from "./components/Game";
import DarkSquare from "./components/DarkSquare";


export default () =>
  <Switch>
    <Route path="/" exact component={Home} />
    <Route path="/login" exact component={Login} />
    <Route path="/register" exact component={Register} />
    <Route path="/game" exact component={Game}/>
  </Switch>;