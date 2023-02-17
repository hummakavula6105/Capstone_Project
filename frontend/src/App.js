// General Imports
import { Routes, Route } from "react-router-dom";
import "./App.css";

// Pages Imports
import HomePage from "./pages/HomePage/HomePage";
import LoginPage from "./pages/LoginPage/LoginPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";
import MyChangeRequests from "./pages/MyChangeRequestsPage/MyChangeRequests";
import NewRequest from "./pages/NewRequestPage/NewRequest";

// Component Imports
import Navbar from "./components/NavBar/NavBar";
import Footer from "./components/Footer/Footer";

// Util Imports
import PrivateRoute from "./utils/PrivateRoute";
import { useEffect, useState } from "react";
import useAuth from "./hooks/useAuth";
import axios from "axios";

const App = () => {
  const [requests, setRequests] = useState([]);
  const [requestId, setRequestId] = useState("");
  const [query, setQuery] = useState("");
  const [user, token] = useAuth();
  useEffect(() => {}, [requests]);
  const getRequests = async () => {
    await axios
    .get(
      `http://127.0.0.1:8000/api/requests/`
    )
    .then((res) => {
      setRequests(res.data.items);
    });
  };
  const changeRequest = (request) => {
    setRequestId(request.target.id);
  }
  return (
    <div>
      <Navbar query={query} setQuery={setQuery}/>
      <Routes>
        <Route
          path="/"
          element={
            <PrivateRoute>
              <HomePage />
            </PrivateRoute>
          }
        />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/new_request" element={<NewRequest/>} />
        <Route path="/my_change_requests" element={<MyChangeRequests/>} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
