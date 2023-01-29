import { useState } from "react";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { Toaster } from "react-hot-toast";
import "./App.css";

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <h1>Welcome to MindMate</h1>,
      errorElement: <h1>404 Not Found</h1>,
    },
  ]);

  return (
    <>
      <Toaster
        position="top-right"
        reverseOrder={false}
        toastOptions={{
          style: {
            fontSize: "14px",
          },
        }}
      />
      <RouterProvider router={router} />
    </>
  );
}

export default App;
