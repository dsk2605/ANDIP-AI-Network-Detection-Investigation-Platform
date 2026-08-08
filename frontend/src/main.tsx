import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import "./index.css";

import App from "./App";

import QueryProvider from "@/app/providers/QueryProvider";

ReactDOM.createRoot(
  document.getElementById("root")!
).render(

  <React.StrictMode>

    <BrowserRouter>

      <QueryProvider>

        <App />

      </QueryProvider>

    </BrowserRouter>

  </React.StrictMode>

);