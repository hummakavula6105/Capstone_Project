import React from 'react';
import EditReqStyler from './EditReqStyler';
import styled from 'styled-components';

const FlexContainer = styled.ul`
display:flex;
flex-wrap: wrap;
`

const RequestMapper = ({requestArray, changeRequest}) => {
    return ( 
        <FlexContainer>
            {requestArray.map(el => <EditReqStyler key={el.id.requestId} request = {el} changeRequest={changeRequest}/>)}
        </FlexContainer>
    );
}
 
export default RequestMapper;