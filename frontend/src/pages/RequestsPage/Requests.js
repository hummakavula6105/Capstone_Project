import React from "react";
import styled from "styled-components";

const FlexContainer = styled.ul`
display:flex;
flex-wrap: wrap;
flex-direction: column;
place-content: top;
justify-content: flex-start;
align-content: flex start;
`

const Requests = ({requests}) => {
  return (
      <FlexContainer>
        {requests.map(request =>  <li key = {request.id} >{request.text}</li>) }
      </FlexContainer>
  );
};

export default Requests;