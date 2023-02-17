import React, { useState } from "react";
import axios from "axios";

import useAuth from "../../hooks/useAuth";


const NewRequest = () => {
  const [request, setRequest] = useState("");
  const [user, token] = useAuth();

  const handleSubmit = async(event)=> {
    event.preventDefault();
    let newRequest = {
      user_id: user.id,
      request_id: requestId,
      area: area,
      description: description,
    };
    let response = await axios.post(`http://127.0.0.1:8000/api/requests/` , newRequest , {headers:{Authorization: `Bearer ${token}`}})
    console.log(response.data);
    NewRequest();
  }

  return (
    <form onSubmit={handleSubmit} className="form-grid">
      <section className="main section">
        <div>
          <label>New Request</label>
          <input
            type="text"
            value={request}
            onChange={(event) => setRequest(event.target.value)}
          />
        </div>
        <div>
          <ButtonHandler
            type="submit"
            className="btn btn-primary"
            style={{ marginTop: "1em" }}
          >
            Submit
          </ButtonHandler>
          <div></div>
        </div>
      </section>
    </form>
  );
};

export default NewRequest;
