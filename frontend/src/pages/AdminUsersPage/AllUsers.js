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

const AllUsers = ({AllUsers}) => {
  return (
      <FlexContainer>
        {AllUsers.map(user =>  <li key = {user.id} >{user.text}</li>) }
      </FlexContainer>
  );
};

export default AllUsers;