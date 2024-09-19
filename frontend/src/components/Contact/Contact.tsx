import { Container } from "./styles";
import emailIcon from "../../assets/email-icon.svg";
import phoneIcon from "../../assets/phone-icon.svg"

export function Contact(){

  return(
    <Container id="contact">
      <header>
        <h2>Contact</h2>
      </header>
      <div className="contacts">
        <div>
        <a href="mailto:Hello@vinayaksingh.com"><img src={emailIcon} alt="Email" /></a> 
          <a href="mailto:Hello@vinayaksingh.com">joanne.christina6@gmail.com</a>
        </div>
        <div>
        <a href="tel:+919630576848"><img src={phoneIcon} alt="Phone No" /></a>
          <a href="tel:+919630576848">(+65) 94548327</a>
        </div>  
      </div>
    </Container>
  )
}